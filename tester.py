#!/usr/bin/env python3
"""
Testeur Printf — version colorée et modulaire
Chaque fichier de tests se trouve dans tests/ et expose TESTS = [(nom, code_C), ...]
Usage :
    ./tester.py /chemin/vers/printf [--verbose] [--list] [--run PATTERN] [--no-color]
"""
import os, sys, subprocess, time, importlib.util, shutil, datetime, logging
from pathlib import Path

# ===============================================================
# 🔧 Configuration - Modifie ces variables pour adapter à ton projet
# ===============================================================

# Nom de la fonction à tester
FUNCTION_NAME = "ft_printf"

# Nom du projet (pour les logs)
PROJECT_NAME = "printferator"

# Module de tests à charger (fichier dans tests/ sans .py)
TEST_MODULE = "t_printf"

# Timeout par défaut (secondes)
DEFAULT_TIMEOUT = 5

# Extensions de fichiers source
SOURCE_EXTENSIONS = [".c", ".h"]

# ===============================================================
# Pour adapter à un autre projet, change juste ces valeurs :
# FUNCTION_NAME = "ft_atoi"
# PROJECT_NAME = "atoiterator"
# TEST_MODULE = "t_atoi"
# DEFAULT_TIMEOUT = 2
# ===============================================================

# ===============================================================
# 🎨 Pretty print (sans dépendances externes)
# ===============================================================
USE_COLOR = sys.stdout.isatty() and "--no-color" not in sys.argv
def C(code): return f"\033[{code}m" if USE_COLOR else ""
CLR = {
    "dim": C("2"),
    "reset": C("0"),
    "cyan": C("36"),
    "green": C("32"),
    "red": C("31"),
    "yellow": C("33"),
    "bold": C("1"),
    "gray": C("90"),
}
def icon(status):
    if status == "PASS": return "✅"
    if status == "FAIL": return "❌"
    if status == "LEAK": return "🚰"  # Icône pour les fuites mémoire
    if status == "TIMEOUT": return "⏰"  # Icône pour les timeouts
    return "💥"
def color_status(s):
    if s == "PASS": return f"{CLR['green']}{s}{CLR['reset']}"
    if s == "FAIL": return f"{CLR['red']}{s}{CLR['reset']}"
    if s == "LEAK": return f"{CLR['red']}{s}{CLR['reset']}"  # Rouge pour les fuites
    if s == "TIMEOUT": return f"{CLR['yellow']}{s}{CLR['reset']}"  # Jaune pour les timeouts
    return f"{CLR['yellow']}{s}{CLR['reset']}"
def human_ms(ms): return f"{ms} ms"

# ===============================================================
# 📝 Système de logging
# ===============================================================
def setup_logging(out_dir):
    """Configure le système de logging pour enregistrer tous les résultats."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = out_dir / f"{PROJECT_NAME}_{timestamp}.log"

    # Configuration du logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
        ]
    )

    logger = logging.getLogger(PROJECT_NAME)
    logger.info("=" * 80)
    logger.info(f"NOUVELLE SESSION {PROJECT_NAME.upper()} 2025")
    logger.info(f"Testing function: {FUNCTION_NAME}")
    logger.info("=" * 80)

    return log_file, logger

def log_norminette_result(logger, result, output, error):
    """Enregistre les résultats de la norminette."""
    logger.info("NORMINETTE CHECK:")
    if result == 0:
        logger.info("✅ NORMINETTE: PASS")
    else:
        logger.error("❌ NORMINETTE: FAIL")
        if output:
            logger.error(f"Sortie norminette:\n{output}")
        if error:
            logger.error(f"Erreur norminette:\n{error}")

def log_test_result(logger, test_name, status, duration, error_output=None):
    """Enregistre le résultat d'un test."""
    if status == "PASS":
        status_icon = "✅"
    elif status == "TIMEOUT":
        status_icon = "⏰"
    else:
        status_icon = "❌"

    logger.info(f"{status_icon} {test_name}: {status} ({duration} ms)")
    if error_output:
        logger.error(f"Erreur de compilation pour {test_name}:\n{error_output}")
    if status == "TIMEOUT":
        logger.warning(f"⚠️ Test {test_name} interrompu après timeout - possible boucle infinie")

def log_compilation_result(logger, success, output=None, error=None):
    """Enregistre les résultats de compilation."""
    if success:
        logger.info("✅ COMPILATION: SUCCESS")
    else:
        logger.error("❌ COMPILATION: FAILED")
        if output:
            logger.error(f"Sortie compilation:\n{output}")
        if error:
            logger.error(f"Erreur compilation:\n{error}")

# ===============================================================
# 🎨 En-tête du programme
# ===============================================================
def print_header():
    """Affiche l'en-tête stylisé du programme."""
    print(f"{CLR['red']}╔═════════════════════════════════════════════════════════════════════════════════╗{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}{CLR['bold']}                               Printferator 2025{CLR['reset']}{CLR['red']}                                 ║{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}                          Testeur complet pour Printf                            {CLR['red']}║{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}{CLR['dim']}                            259 tests • 4 sections{CLR['reset']}{CLR['red']}                               ║{CLR['reset']}")
    print(f"{CLR['red']}╚═════════════════════════════════════════════════════════════════════════════════╝{CLR['reset']}")
    print()

    # Guide des commandes disponibles
    print(f"{CLR['dim']}Commandes disponibles :{CLR['reset']}")
    print(f"  {CLR['cyan']}./tester.py /path/printf{CLR['reset']}                - Exécuter tous les tests")
    print(f"  {CLR['cyan']}./tester.py /path/printf --list{CLR['reset']}         - Lister tous les tests disponibles")
    print(f"  {CLR['cyan']}./tester.py /path/printf --run PATTERN{CLR['reset']}  - Exécuter les tests contenant PATTERN")
    print(f"  {CLR['cyan']}./tester.py /path/printf --verbose{CLR['reset']}      - Mode verbose (plus de détails)")
    print(f"  {CLR['cyan']}./tester.py /path/printf --no-color{CLR['reset']}     - Désactiver les couleurs")
    print(f"  {CLR['cyan']}./tester.py /path/printf --timeout N{CLR['reset']}    - Timeout de N secondes (défaut: {DEFAULT_TIMEOUT}s)")
    print(f"  {CLR['cyan']}./tester.py /path/printf --clear{CLR['reset']}        - Nettoyer le dossier build avant les tests")
    print(f"")
    print(f"{CLR['dim']}Exemples :{CLR['reset']}")
    print(f"  {CLR['yellow']}./tester.py ./printf --run basic{CLR['reset']}        - Tester les formats de base")
    print(f"  {CLR['yellow']}./tester.py ./printf --run hex{CLR['reset']}          - Tester les formats hexadécimaux")
    print(f"  {CLR['yellow']}./tester.py ./printf --run edge{CLR['reset']}         - Tester les cas limites")
    print(f"  {CLR['yellow']}./tester.py ./printf --timeout 10{CLR['reset']}       - Timeout de 10 secondes par test")
    print()

    # Informations GitHub
    print(f"{CLR['dim']}─────────────────────────────────────────────────────────────────────────────────{CLR['reset']}")
    print(f"{CLR['dim']}Développé par{CLR['reset']} {CLR['bold']}Blaeste{CLR['reset']}")
    print(f"{CLR['dim']}GitHub:{CLR['reset']} {CLR['cyan']}https://github.com/Blaeste{CLR['reset']}")
    print(f"{CLR['dim']}Projet:{CLR['reset']} {CLR['cyan']}https://github.com/Blaeste/printferator{CLR['reset']}")
    print()

# ===============================================================
# ⚙️ Args
# ===============================================================
VERBOSE = "--verbose" in sys.argv
RUN_FILTER = None
LIST_ONLY = False
SAFE_MODE = False
TIMEOUT = DEFAULT_TIMEOUT  # Utilise la configuration du projet

argv = []
i = 1
while i < len(sys.argv):
    a = sys.argv[i]
    if a == "--verbose":
        VERBOSE = True
    elif a == "--list":
        LIST_ONLY = True
    elif a == "--run" and i + 1 < len(sys.argv):
        RUN_FILTER = sys.argv[i + 1]
        i += 1
    elif a == "--safe":
        SAFE_MODE = True
    elif a == "--timeout" and i + 1 < len(sys.argv):
        try:
            TIMEOUT = int(sys.argv[i + 1])
            if TIMEOUT <= 0:
                print("Erreur: Le timeout doit être un nombre positif")
                sys.exit(1)
        except ValueError:
            print("Erreur: Le timeout doit être un nombre entier")
            sys.exit(1)
        i += 1
    elif a == "--clear":
        # Nettoyer plusieurs dossiers avant de continuer
        root = Path(__file__).resolve().parent
        dirs_to_clean = [
            root / "build",
            root / "out",
            root / "tests" / "__pycache__"
        ]

        cleaned_dirs = []
        for dir_path in dirs_to_clean:
            if dir_path.exists():
                shutil.rmtree(dir_path)
                cleaned_dirs.append(dir_path.name)

        if cleaned_dirs:
            print(f"{CLR['cyan']}🧹 Dossiers nettoyés: {', '.join(cleaned_dirs)}{CLR['reset']}")
        else:
            print(f"{CLR['dim']}ℹ️  Tous les dossiers sont déjà propres{CLR['reset']}")
    else:
        argv.append(a)
    i += 1

if len(argv) < 1:
    print("Usage: ./tester.py /chemin/vers/printf [--verbose] [--list] [--run PATTERN] [--no-color] [--safe] [--timeout SECONDS] [--clear]")
    sys.exit(1)

printf = Path(argv[0]).resolve()

# ===============================================================
# 🧹 Norminette — config
# ===============================================================
# Laisse None pour auto-détection (privilégie ./normiette s'il existe).
NORM_CMD = "./normiette"   # ex: "./normiette" ou "./norminette"
NORM_FLAGS = "-R CheckForbiddenSourceHeader"   # ex: '-R CheckForbiddenSourceHeader'


# ===============================================================
# 🧰 Utils
# ===============================================================
def sh(cmd, silent=not VERBOSE):
    try:
        if silent:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n{CLR['red']}[ERREUR] Commande échouée:{CLR['reset']} {' '.join(cmd)}")
        if e.stdout:
            print(e.stdout.decode(errors="ignore"))
        raise

def ensure_path(p: Path, kind: str):
    if not p.exists():
        print(f"{CLR['red']}Erreur:{CLR['reset']} {kind} introuvable: {p}")
        sys.exit(2)

def check_makefile_rules():
    """Vérifie les règles du Makefile et affiche un rapport formaté."""
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}|{' '*30}COMPILING PRINTF{' '*35}|{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")

    rules = ["all", "$(NAME)", "fclean", "re", "clean", "bonus"]
    statuses = []

    for rule in rules:
        try:
            if rule in ["all", "$(NAME)"]:
                # Tester la compilation
                result = subprocess.run(
                    ["make", "-C", str(printf), rule if rule != "$(NAME)" else "all"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la compilation
                )
                # Vérifier que le fichier libftprintf.a existe
                if result.returncode == 0 and (printf / "libftprintf.a").exists():
                    statuses.append("ok")
                else:
                    statuses.append("error")
            elif rule == "clean":
                result = subprocess.run(
                    ["make", "-C", str(printf), "clean"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT
                )
                statuses.append("ok" if result.returncode == 0 else "error")
            elif rule == "fclean":
                result = subprocess.run(
                    ["make", "-C", str(printf), "fclean"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT
                )
                statuses.append("ok" if result.returncode == 0 else "error")
            elif rule == "re":
                result = subprocess.run(
                    ["make", "-C", str(printf), "re"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la recompilation
                )
                if result.returncode == 0 and (printf / "libftprintf.a").exists():
                    statuses.append("ok")
                else:
                    statuses.append("error")
            elif rule == "bonus":
                result = subprocess.run(
                    ["make", "-C", str(printf), "bonus"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la compilation bonus
                )
                if result.returncode == 0:
                    statuses.append("ok")
                else:
                    statuses.append("missing")
            else:
                statuses.append("unknown")

        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            statuses.append("error")

    # Affichage du rapport
    print("rules:")

    # Ligne des noms de règles
    rule_line = ""
    for rule in rules:
        if len(rule) <= 10:
            rule_line += f"{rule:<10} "
        else:
            rule_line += f"{rule:<15} "
    print(rule_line.rstrip())

    # Ligne des statuts avec couleurs
    status_line = ""
    for i, status in enumerate(statuses):
        rule = rules[i]
        if status == "ok":
            colored_status = f"{CLR['green']}ok{CLR['reset']}"
        elif status == "missing":
            colored_status = f"{CLR['yellow']}missing{CLR['reset']}"
        elif status == "found":
            colored_status = f"{CLR['cyan']}found{CLR['reset']}"
        else:
            colored_status = f"{CLR['red']}error{CLR['reset']}"

        if len(rule) <= 10:
            status_line += f"{colored_status:<19} "  # 19 pour compenser les codes couleur
        else:
            status_line += f"{colored_status:<24} "

    print(status_line.rstrip())
    print()

def build_printf():
    left = " [build] printf "
    dots = "." * max(1, 75 - len(left) - 10)
    print(f"{CLR['dim']}{left}{dots}{CLR['reset']}", end="", flush=True)

    try:
        # Compiler d'abord la partie obligatoire
        subprocess.run(["make", "-C", str(printf), "re"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        ensure_path(printf / "libftprintf.a", "libftprintf.a")

        # Essayer de compiler les bonus aussi (si ils existent)
        try:
            subprocess.run(["make", "-C", str(printf), "bonus"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        except subprocess.CalledProcessError:
            # Les bonus ne sont peut-être pas disponibles, ce n'est pas grave
            pass

        print(f" {icon('PASS')} {color_status('PASS')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f" {icon('FAIL')} {color_status('FAIL')}")
        print(f"Erreur de compilation: {e}")
        return False

# ===============================================================
# 🎯 Détection des sections du sujet
# ===============================================================
def get_section_info(test_name, previous_test_name=None):
    """Détermine si un test marque le début d'une nouvelle section."""

    # Mapping des fonctions vers les sections pour printf
    basic_functions = [
        'printf'  # Tous les tests printf
    ]

    def get_function_from_test(name):
        return name.split('/')[0]

    current_func = get_function_from_test(test_name)

    # Déterminer la section actuelle pour printf
    if current_func in basic_functions:
        section = "PRINTF"
        desc = "Tests de ft_printf"
    else:
        return None, None, None

    # Pour printf, on n'a qu'une seule section, donc on l'affiche au début
    if previous_test_name is None:
        return section, desc, True

    return section, desc, False

def print_section_header(section, description):
    """Affiche un en-tête de section."""
    print()
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}🔹 {section} — {description}{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print()

def print_subsection_header(subsection, description):
    """Affiche un en-tête de sous-section."""
    print()
    print(f"{CLR['dim']}{'─'*60}{CLR['reset']}")
    print(f"{CLR['cyan']}📂 {subsection} — {description}{CLR['reset']}")
    print(f"{CLR['dim']}{'─'*60}{CLR['reset']}")
    print()

def get_subsection_info(test_name, previous_test_name):
    """Détermine si on doit afficher une nouvelle sous-section."""
    subsection_descriptions = {
        # PRINTF
        'printf': 'Tests de ft_printf',

        # Types de tests printf
        'basic': 'Tests de base',
        'edge': 'Cas limites',
        'hex': 'Formats hexadécimaux',
        'mixed': 'Formats combinés',
        'pointer': 'Pointeurs',
        'unsigned': 'Non signés',
        'percent': 'Caractère %',
        'null': 'Valeurs nulles',
        'return': 'Valeurs de retour',

        # Tests avancés
        'valgrind': 'Tests de fuites mémoire',
        'stress': 'Tests de stress',
    }

    current_subsection = test_name.split('/')[0]

    if previous_test_name:
        previous_subsection = previous_test_name.split('/')[0]
        if current_subsection != previous_subsection:
            description = subsection_descriptions.get(current_subsection, current_subsection)
            return current_subsection, description, True
    else:
        # Premier test
        description = subsection_descriptions.get(current_subsection, current_subsection)
        return current_subsection, description, True

    return current_subsection, None, False

# ===============================================================
# 🧱 Compilation et exécution
# ===============================================================
def compile_harness(root: Path, name: str, source: str, logger=None) -> Path:
    src = root / "build" / f"{name}.c"
    exe = root / "build" / name

    # préambule minimal: stdio pour fprintf et ft_printf.h si absent
    prelude = '#include <stdio.h>\n'
    if '#include "ft_printf.h"' not in source:
        prelude += '#include "ft_printf.h"\n'
    source = prelude + source

    src.write_text(source)

    # Discover include directories: prefer standard locations and any folder containing ft_printf.h
    include_dirs = [str(printf)]  # Always include the printf root directory first

    # Check for common include directory names
    common_inc_names = ["inc", "include", "includes", "headers"]
    for inc_name in common_inc_names:
        p = printf / inc_name
        if p.is_dir():
            include_dirs.append(str(p))

    # Also scan all subdirectories for ft_printf.h and add their parent dir
    try:
        for header_file in printf.rglob("ft_printf.h"):
            parent = header_file.parent
            parent_str = str(parent)
            if parent_str not in include_dirs:
                include_dirs.append(parent_str)
    except Exception:
        pass

    inc_flags = [f"-I{p}" for p in include_dirs]
    lib = "-L" + str(printf)
    cmd = [os.environ.get("CC", "cc"), "-Wall", "-Wextra", "-Werror"] + inc_flags + [str(src), lib, "-lftprintf", "-o", str(exe)]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            if logger:
                log_compilation_result(logger, True)
        else:
            if logger:
                log_compilation_result(logger, False, result.stdout, result.stderr)
            sh(cmd)  # Original behavior for errors
    except Exception as e:
        if logger:
            log_compilation_result(logger, False, error=str(e))
        sh(cmd)  # Fallback to original behavior

    return exe

# ===============================================================
# 🧩 Chargement des fichiers de tests
# ===============================================================
# 🧩 Chargement des fichiers de tests
# ===============================================================
def load_tests(tests_dir: Path):
    """Charge les tests selon la configuration du projet"""

    all_tests = []

    # Charge le module de tests principal
    test_file = f"{TEST_MODULE}.py"
    file_path = tests_dir / test_file

    if file_path.exists():
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "TESTS"):
            all_tests.extend(mod.TESTS)
    else:
        print(f"⚠️  Fichier de tests non trouvé: {file_path}")

    # Charge tous les autres fichiers de tests dans le dossier
    loaded_files = {test_file}
    for file in sorted(tests_dir.glob("t_*.py")):
        if file.name not in loaded_files:
            try:
                spec = importlib.util.spec_from_file_location(file.stem, file)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "TESTS"):
                    all_tests.extend(mod.TESTS)
            except Exception as e:
                print(f"⚠️  Erreur lors du chargement de {file.name}: {e}")

    return all_tests# ===============================================================
# 🚴‍♂️ Exécution d'un binaire de test
# ===============================================================
def run_exec(exe: Path, test_name=""):
    t0 = time.time()

    # Utiliser le timeout configuré globalement, avec des valeurs spéciales pour certains tests
    default_timeout = TIMEOUT
    valgrind_timeout = TIMEOUT * 3  # Plus long timeout pour valgrind
    crash_timeout = min(2, TIMEOUT)  # Timeout court pour les tests de crash (max 2s)

    # Pour les tests valgrind, lancer avec valgrind pour détecter les fuites mémoire
    if "valgrind" in test_name:
        # Vérifier si valgrind est disponible
        try:
            subprocess.run(["valgrind", "--version"], capture_output=True, check=True)
            valgrind_available = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            valgrind_available = False

        if valgrind_available:
            # Lancer avec valgrind
            valgrind_cmd = [
                "valgrind",
                "--tool=memcheck",
                "--leak-check=full",
                "--show-leak-kinds=all",
                "--track-origins=yes",
                "--error-exitcode=42",  # Code de sortie spécial en cas de fuite
                "--quiet",  # Réduire le bruit
                str(exe)
            ]
            try:
                res = subprocess.run(valgrind_cmd, timeout=valgrind_timeout)
                ms = int((time.time() - t0) * 1000)
                # Code 42 = fuite détectée, Code 0 = pas de fuite
                return res.returncode, ms
            except subprocess.TimeoutExpired:
                ms = int((time.time() - t0) * 1000)
                return -999, ms  # Code spécial pour timeout
        else:
            # Valgrind non disponible, exécuter normalement avec timeout
            try:
                res = subprocess.run([str(exe)], timeout=default_timeout)
                ms = int((time.time() - t0) * 1000)
                return res.returncode, ms
            except subprocess.TimeoutExpired:
                ms = int((time.time() - t0) * 1000)
                return -999, ms  # Code spécial pour timeout

    # Pour les tests d'overprotection, on s'attend à un crash (SIGSEGV)
    elif "overprotection" in test_name and "should_crash" in test_name:
        # Timeout plus court pour les tests de crash
        try:
            res = subprocess.run([str(exe)], timeout=crash_timeout)
            ms = int((time.time() - t0) * 1000)
            return res.returncode, ms
        except subprocess.TimeoutExpired:
            # Si le test timeout, c'est probablement parce qu'il attend un signal
            ms = int((time.time() - t0) * 1000)
            return 1, ms  # FAIL - le test n'a pas crashé comme attendu
    else:
        # Tests normaux avec timeout de protection
        try:
            res = subprocess.run([str(exe)], timeout=default_timeout)
            ms = int((time.time() - t0) * 1000)
            return res.returncode, ms
        except subprocess.TimeoutExpired:
            ms = int((time.time() - t0) * 1000)
            return -999, ms  # Code spécial pour timeout

# ===============================================================
# 🧹 Norminette — détection + exécution
# ===============================================================
def _detect_norm_cmd():
    # Ordre de préférence : ./normiette, ./norminette, binaire système
    candidates = []
    if NORM_CMD:
        candidates.append(NORM_CMD)
    candidates += ["./normiette", "./norminette", "./norminette.py",
                   "norminette", "python3 -m norminette", "pipx run norminette"]
    for cand in candidates:
        if " " in cand:
            prog = cand.split()[0]
        else:
            prog = cand
        if "/" in prog:
            p = Path(prog)
            if p.exists() and os.access(p, os.X_OK):
                return cand.split(), cand
        else:
            found = shutil.which(prog)
            if found:
                return cand.split(), cand
    return None, None

def run_norminette(log_path: Path, logger=None):
    cmd_list, printable = _detect_norm_cmd()
    start = time.time()
    if not cmd_list:
        # Pas trouvé → on marque SKIP mais on n'arrête rien
        result = {"status":"SKIP","ms":int((time.time()-start)*1000),"detail":"norminette introuvable"}
        if logger:
            logger.warning("⚠️ NORMINETTE: SKIP - norminette introuvable")
        return result

    args = cmd_list[:]
    if NORM_FLAGS:
        args.extend(NORM_FLAGS.split())

    # Au lieu d'analyser tout le dossier, analyser seulement les fichiers .c et .h
    # pour éviter les fichiers de test comme tester.py
    c_files = list(printf.glob("*.c"))
    h_files = list(printf.glob("*.h"))

    # Aussi chercher dans les sous-dossiers standards (src/, include/, etc.)
    for subdir in ["src", "srcs", "sources", "include", "includes", "inc", "headers"]:
        subdir_path = printf / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            c_files.extend(subdir_path.glob("*.c"))
            h_files.extend(subdir_path.glob("*.h"))

    all_files = c_files + h_files

    if not all_files:
        # Aucun fichier .c/.h trouvé, fallback vers le dossier complet
        # mais avec exclusions explicites pour les dossiers de test
        args.append(str(printf))

        # Ajouter des exclusions explicites si la norminette les supporte
        test_dirs_to_exclude = ["libfterator", "tests", "test", ".git", "__pycache__", "out"]
        test_files_to_exclude = ["tester.py", "*.py", "*.pyc"]

        # Essayer d'ajouter --exclude pour chaque pattern (certaines versions de norminette le supportent)
        for exclude in test_dirs_to_exclude + test_files_to_exclude:
            exclude_path = printf / exclude.rstrip('*')
            if exclude_path.exists() or exclude in ["*.py", "*.pyc", "tester.py"]:
                # Ajouter l'exclusion (silencieusement - certaines norminettes ne supportent pas --exclude)
                try:
                    if '--exclude' not in args:  # Éviter les doublons
                        args.extend(['--exclude', exclude])
                except:
                    pass  # Ignorer si --exclude n'est pas supporté
    else:
        # Ajouter tous les fichiers .c et .h trouvés
        for file in all_files:
            args.append(str(file))

    try:
        proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, text=True)
        out = proc.stdout or ""
        error = ""
    except Exception as e:
        out = f"Erreur de lancement: {e}\n"
        error = str(e)
        proc = type("X", (), {"returncode":1})()

    # Écrit le log complet
    log_path.write_text(out)

    # Heuristique simple pour l'état
    text = (out or "").lower()
    failed = ("error" in text) or ("ko" in text) or (proc.returncode != 0)
    status = "FAIL" if failed else "PASS"
    ms = int((time.time()-start)*1000)

    # Log des résultats de la norminette
    if logger:
        log_norminette_result(logger, proc.returncode, out, error)

    return {"status": status, "ms": ms, "detail": out}


# ===============================================================
# 🚀 Main
# ===============================================================
def main():
    print_header()

    root = Path(__file__).resolve().parent
    tests_dir = root / "tests"
    ensure_path(printf / "Makefile", "Makefile printf")

    (root / "build").mkdir(exist_ok=True)
    (root / "out").mkdir(exist_ok=True)

    # Configuration du logging dans le dossier out/
    log_file, logger = setup_logging(root / "out")

    # --- Norminette obligatoire, non bloquante ---
    norm_log = (root / "out" / "norminette.txt")

    # Affichage formaté de la Norminette
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}|{' '*29}NORMINETTE CHECK{' '*36}|{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")

    left = " [norm] check "
    dots = "." * max(1, 75 - len(left) - 10)
    print(f"{CLR['dim']}{left}{dots}{CLR['reset']}", end="", flush=True)

    norm = run_norminette(norm_log, logger)
    print(f" {icon(norm['status'])} {color_status(norm['status'])} " +
          f"{CLR['gray']}({human_ms(norm['ms'])}){CLR['reset']}")
    print()


    tests = load_tests(tests_dir)
    if not tests:
        print("Aucun test trouvé dans tests/")
        return

    # Filtre optionnel
    if RUN_FILTER:
        tests = [t for t in tests if RUN_FILTER in t[0]]
        if not tests:
            print(f"Aucun test ne correspond au filtre: {RUN_FILTER}")
            return

    if LIST_ONLY:
        for name, _ in tests:
            print(name)
        return

    check_makefile_rules()

    # Compiler le projet
    if not build_printf():
        print(f"{CLR['red']}❌ Compilation échouée. Arrêt du test.{CLR['reset']}")
        sys.exit(1)    # -----------------------------------------------------------
    # RUN + affichage joli
    # -----------------------------------------------------------
    total = len(tests)
    rows = []
    print()
    print(f"{CLR['bold']}Running {total} test(s){CLR['reset']} {CLR['dim']}(timeout: {TIMEOUT}s){CLR['reset']}")

    previous_test_name = None
    for idx, (name, src) in enumerate(tests, 1):
        # Vérifier si on doit afficher un nouveau header de section
        section, desc, is_new_section = get_section_info(name, previous_test_name)
        if is_new_section and section:
            print_section_header(section, desc)

        # Vérifier si on doit afficher un nouveau header de sous-section
        subsection, subsec_desc, is_new_subsection = get_subsection_info(name, previous_test_name)
        if is_new_subsection and subsection and subsec_desc:
            print_subsection_header(subsection, subsec_desc)

        safe = name.replace('/', '_')
        left = f" [{idx:>2}/{total}] {name} "
        dots = "." * max(1, 77 - len(left) - 10)
        print(f"{CLR['dim']}{left}{dots}{CLR['reset']}", end="", flush=True)

        exe = compile_harness(root, safe, src, logger)

        # Capturer la sortie du test pour l'afficher après le résultat
        test_output = ""
        if exe and exe.exists():
            try:
                result = subprocess.run([str(exe)], capture_output=True, text=True, timeout=TIMEOUT)
                test_output = result.stdout if result.stdout else ""
                code = result.returncode
                ms = 1  # Placeholder pour timing
            except subprocess.TimeoutExpired:
                code = -999
                ms = TIMEOUT * 1000
            except Exception:
                code = -1
                ms = 1
        else:
            code = -1
            ms = 1

        # Vérifier d'abord si c'est un timeout
        if code == -999:
            status = "TIMEOUT"
        # Logique spéciale pour les tests valgrind
        elif "valgrind" in name:
            # Code 0 = pas de fuite (PASS), Code 42 = fuite détectée (FAIL), autres = erreur d'exécution
            if code == 0:
                status = "PASS"
            elif code == 42:
                status = "LEAK"  # Fuite mémoire détectée
            else:
                status = "FAIL"  # Erreur d'exécution
        # Logique spéciale pour les tests d'overprotection
        elif "overprotection" in name and "should_crash" in name:
            # Pour ces tests, on s'attend à un code de retour 0 (PASS = a crashé comme attendu)
            # Code 1 = FAIL (sur-protégé, n'a pas crashé)
            status = "PASS" if code == 0 else "FAIL"
        else:
            status = "PASS" if code == 0 else ("CRASH" if code not in (0, 1) else "FAIL")

        # Log du résultat du test
        error_output = None
        if status != "PASS":
            # Capturer l'erreur si le test a échoué
            if exe.exists():
                try:
                    error_result = subprocess.run([str(exe)], capture_output=True, text=True, timeout=TIMEOUT)
                    if error_result.stdout or error_result.stderr:
                        error_output = f"stdout: {error_result.stdout}\nstderr: {error_result.stderr}"
                except:
                    pass

        log_test_result(logger, name, status, ms, error_output)

        print(f" {icon(status)} {color_status(status)} {CLR['gray']}({human_ms(ms)}){CLR['reset']}")

        # Afficher la sortie du test après le résultat
        if test_output.strip():
            output = test_output.rstrip()

            # Essayer de séparer les sorties de printf et ft_printf
            lines = output.split('\n')

            if len(lines) == 2 and lines[0] == lines[1]:
                # Cas classique : printf et ft_printf donnent exactement la même sortie
                print(f"{CLR['dim']}    printf():    {lines[0]}{CLR['reset']}")
                print(f"{CLR['dim']}    ft_printf(): {lines[1]}{CLR['reset']}")
            elif len(lines) >= 2:
                # Plusieurs lignes : essayer de les associer intelligemment
                mid = len(lines) // 2
                printf_lines = lines[:mid]
                ft_printf_lines = lines[mid:]

                print(f"{CLR['dim']}    printf():    {' | '.join(printf_lines)}{CLR['reset']}")
                print(f"{CLR['dim']}    ft_printf(): {' | '.join(ft_printf_lines)}{CLR['reset']}")
            else:
                # Une seule ligne : essayer plusieurs méthodes de séparation

                # Méthode 1 : Couper exactement en deux si les motifs sont identiques
                half_len = len(output) // 2
                if len(output) > 2 and output[:half_len] == output[half_len:]:
                    printf_part = output[:half_len]
                    ft_printf_part = output[half_len:]
                    print(f"{CLR['dim']}    printf():    {printf_part}{CLR['reset']}")
                    print(f"{CLR['dim']}    ft_printf(): {ft_printf_part}{CLR['reset']}")

                # Méthode 2 : Chercher un motif répété avec de petites variations (ex: adresses)
                elif len(output) > 20:  # Seulement pour les sorties longues
                    # Essayer de trouver le point de séparation en cherchant des patterns similaires
                    # Heuristique : chercher où le pattern se répète avec variations
                    best_split = None
                    best_similarity = 0

                    # Tester différents points de coupe autour du milieu
                    for split_point in range(max(1, half_len - 10), min(len(output), half_len + 10)):
                        part1 = output[:split_point]
                        part2 = output[split_point:]

                        # Calculer la similarité en ignorant les adresses hexadécimales
                        import re
                        clean_part1 = re.sub(r'0x[0-9a-fA-F]+', '0xXXXX', part1)
                        clean_part2 = re.sub(r'0x[0-9a-fA-F]+', '0xXXXX', part2)

                        if clean_part1 == clean_part2:
                            best_split = split_point
                            best_similarity = 1.0
                            break

                        # Calculer similarité approximative
                        if len(clean_part1) > 0 and len(clean_part2) > 0:
                            similarity = len(set(clean_part1) & set(clean_part2)) / max(len(set(clean_part1)), len(set(clean_part2)))
                            if similarity > best_similarity and similarity > 0.8:
                                best_similarity = similarity
                                best_split = split_point

                    if best_split and best_similarity > 0.8:
                        printf_part = output[:best_split]
                        ft_printf_part = output[best_split:]
                        print(f"{CLR['dim']}    printf():    {printf_part}{CLR['reset']}")
                        print(f"{CLR['dim']}    ft_printf(): {ft_printf_part}{CLR['reset']}")
                    else:
                        print(f"{CLR['dim']}    sortie: {output}{CLR['reset']}")
                else:
                    print(f"{CLR['dim']}    sortie: {output}{CLR['reset']}")

        rows.append((name, status, ms))

        # Ajouter un peu d'espace entre les tests pour la lisibilité
        print()

        previous_test_name = name

    # -----------------------------------------------------------
    # Résumé final
    # -----------------------------------------------------------
    ok = sum(1 for _, s, _ in rows if s == "PASS")
    fails = [(n, s, m) for n, s, m in rows if s != "PASS"]

    print()
    print(f"{CLR['bold']}Résumé{CLR['reset']} — {CLR['green']}{ok}{CLR['reset']}/{total} PASS")
    if fails:
        print(f"{CLR['red']}Échecs / Crashs:{CLR['reset']}")
        for n, s, m in fails:
            print(f"  - {n:<25} {color_status(s)} {CLR['gray']}({human_ms(m)}){CLR['reset']}")
    else:
        print(f"{CLR['green']}Tous les tests passent.{CLR['reset']}")

    # Log du résumé final
    logger.info("="*50)
    logger.info(f"RÉSUMÉ FINAL: {ok}/{total} tests réussis")
    if fails:
        logger.error("TESTS ÉCHOUÉS:")
        for n, s, m in fails:
            logger.error(f"  - {n}: {s} ({m} ms)")
    logger.info("="*50)

    # Information sur le fichier de log
    print()
    print(f"{CLR['cyan']}📝 Log détaillé sauvegardé dans:{CLR['reset']} {log_file}")
    print(f"{CLR['dim']}   Contient tous les résultats, erreurs et sorties complètes{CLR['reset']}")

# ===============================================================
# 🧠 Entry point
# ===============================================================
if __name__ == "__main__":
    main()
