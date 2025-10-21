# 🚀 Printferator 2025 - Tester Modulaire

[![Tests](https://img.shields.io/badge/Tests-30%2F30-brightgreen)](https://github.com/Blaeste/printferator)
[![Norminette](https://img.shields.io/badge/Norminette-100%25-blue)](https://github.com/42School/norminette)
[![42 School](https://img.shields.io/badge/42-School-000000)](https://42.fr)

> Testeur modulaire et facilement adaptable pour **ft_printf** et d'autres fonctions de l'École 42. Configuration simple par variables.


## ⚡ Installation ultra-rapide (copier/coller)## 🎯 Utilisation Rapide

```bash```bash

git clone https://github.com/Blaeste/printferator.git# Tester ft_printf

cd printferator./tester.py ./printf

```

# Tester avec des options

```bash./tester.py ./printf --verbose

./tester.py /chemin/vers/votre/printf./tester.py ./printf --run "basic"

# Exemple: ./tester.py ../printf./tester.py ./printf --list

``````

**C'est tout ! Aucune dépendance requise.**## 🔧 Adaptation Facile

Fonctionne avec Python 3.6+ (installé par défaut sur les machines 42).

Le tester est **modulaire** et s'adapte facilement à d'autres fonctions en modifiant la configuration :

---

### Pour ft_printf (par défaut)

## ✨ Points forts```python

CONFIG.FUNCTION_NAME = "ft_printf"

- ✅ Norminette intégrée (vérification automatique)CONFIG.PROJECT_NAME = "printferator"

- 🧪 30 tests exhaustifs avec cas limites et edge casesCONFIG.DEFAULT_TEST_MODULE = "t_printf"

- 🔧 **Modulaire** — Facilement adaptable à d'autres projets```

- 🎨 Interface claire avec séparation printf() vs ft_printf()

- 🧾 Logs complets et métriques détaillées### Pour ft_atoi

- ⏱️ Timeout configurable pour éviter les boucles infinies```python



## 🎯 Couverture des tests (30)CONFIG.PROJECT_NAME = "atoiterator"


- 📂 **printf** — Tests de ft_printf: 30 tests```

  - Formats de base: `%c`, `%s`, `%d`, `%i`, `%u`, `%x`, `%X`, `%p`, `%%`

  - Cas limites: `NULL`, valeurs maximales, chaînes vides### Pour toute la libft

  - Edge cases: pointeurs null, caractères spéciaux, formats complexes```python


## 💡 Utilisation rapideCONFIG.PROJECT_NAME = "libfterator"


```bash```

# Lister tous les tests disponibles

./tester.py /chemin/vers/printf --list## 📁 Structure



# Exécuter tous les tests```

./tester.py /chemin/vers/printfprintferator/

├── tester.py              # Script principal (modulaire)

# Exécuter des tests spécifiques├── config_examples.py     # Exemples de configuration

./tester.py /chemin/vers/printf --run basic├── tests/

./tester.py /chemin/vers/printf --run hex│   ├── t_printf.py       # Tests pour ft_printf

./tester.py /chemin/vers/printf --run edge│   ├── t_atoi.py         # Tests pour ft_atoi

│   └── ...               # Autres tests

# Mode verbeux (progression + logs complets)└── printf/               # Ton code ft_printf

./tester.py /chemin/vers/printf --verbose    ├── ft_printf.c

    ├── ft_printf.h

# Désactiver les couleurs (pratique pour les logs CI)    └── Makefile

./tester.py /chemin/vers/printf --no-color```



# Timeout personnalisé## ✨ Fonctionnalités

./tester.py /chemin/vers/printf --timeout 10

```- 🎨 **Interface colorée** avec émojis

- 📊 **Statistiques détaillées** des tests

## 🧰 Options- 🚰 **Détection de fuites mémoire** (valgrind)

- ⏱️ **Timeout configurable** pour éviter les boucles infinies

- `--list`: affiche tous les tests disponibles et leur nom exécutable- 📝 **Logs complets** avec timestamp

- `--run <pattern>`: exécute les tests contenant le pattern (ex: basic, hex, edge)- 🔍 **Filtrage des tests** par pattern

- `--verbose`: affiche la progression détaillée et les logs complets- 🔧 **Configuration modulaire** pour s'adapter à n'importe quelle fonction

- `--no-color`: désactive les couleurs (utile pour la CI/logs)

- `--timeout N`: définit le timeout en secondes (défaut: 5s)## 🚀 Comment Adapter à Une Nouvelle Fonction



## 🌟 Fonctionnalités avancées1. **Modifie la config** dans `tester.py` :

   ```python

### 🔧 Modularité totale   CONFIG.FUNCTION_NAME = "ma_fonction"

Le tester s'adapte facilement à d'autres projets en modifiant 4 variables en haut du fichier :   CONFIG.PROJECT_NAME = "mon_testeur"

```python   CONFIG.DEFAULT_TEST_MODULE = "t_ma_fonction"

FUNCTION_NAME = "ft_printf"    # Nom de ta fonction   ```

PROJECT_NAME = "printf"        # Nom du projet

TEST_MODULE = "t_printf"       # Fichier de tests2. **Crée tes tests** dans `tests/t_ma_fonction.py` :

DEFAULT_TIMEOUT = 5            # Timeout par défaut   ```python

```   TESTS = [

       ("test_nom", '''

### 🎨 Interface lisible   #include <stdio.h>

- Affichage hiérarchique avec sections par fonction (📂)   int main() {

- Séparation claire: `printf():` vs `ft_printf():`       // Ton test ici

- Codes couleur: PASS ✅, FAIL ❌       return 0;  // 0 = succès, 1 = échec

- Compteurs de progression et résumés en fin d'exécution   }'''),

   ]

### 🧾 Système de logs   ```

- Tous les résultats sont sauvegardés dans `out/` avec horodatage

- Logs norminette, compilation, exécution et métriques3. **Lance le tester** :

- Format: `printferator_YYYYMMDD_HHMMSS.log`   ```bash

   ./tester.py /chemin/vers/ton/projet

### 🧩 Compatibilité   ```

- Linux (recommandé) et WSL: support complet

- macOS: fonctionnement OK```bash

- Windows natif: utilisez WSL pour une expérience optimalegit clone https://github.com/Blaeste/libfterator.git

cd libfterator

### 🚀 Adaptation à d'autres projets```

1. **Modifie la config** dans `tester.py` (4 variables en haut)

2. **Crée tes tests** dans `tests/t_mon_projet.py````bash

3. **Lance** : `./tester.py /chemin/vers/ton/projet`./tester.py /chemin/vers/votre/libft

# Exemple: ./tester.py ../libft

### ❓ FAQ rapide```

- Où sont les logs ? Dans le dossier `out/`, avec un horodatage par session.

- Comment adapter à libft ? Modifie les 4 variables de config et crée `tests/t_libft.py`.**C'est tout ! Aucune dépendance requise.**

- Timeout trop court ? Utilise `--timeout N` pour augmenter la limite.Fonctionne avec Python 3.6+ (installé par défaut sur les machines 42).



## 🖥️ Pré-requis---



- Python 3.6+ (par défaut sur Linux des machines 42)## ✨ Points forts

- Environnement POSIX (Linux/WSL conseillé)

- ✅ Norminette intégrée (vérification automatique)

## 🧪 Exemple de sortie (extrait)- 🧪 281 tests exhaustifs avec cas limites et edge cases

- 🔒 Validation de sur-protection (NULL pointers attendus)

```- 🚰 Valgrind intégré avec fallback si non installé

╔═════════════════════════════════════════════════════════════════════════════════╗- 🎨 Interface claire avec sous-sections par fonction

║                               Printferator 2025                                 ║- 🧾 Logs complets et métriques détaillées

║                          Testeur complet pour Printf                            ║

║                            30 tests • 1 section                                 ║## 🎯 Couverture des tests (281)

╚═════════════════════════════════════════════════════════════════════════════════╝

- 📚 Partie 1 — Fonctions de la libc: 149 tests

[norm] check ................................................... ✅ PASS (116 ms)- 🔧 Partie 2 — Fonctions supplémentaires: 80 tests

[build] printf ................................................. ✅ PASS- 🎁 Bonus — Listes chaînées: 19 tests

- 🚰 Valgrind — Fuites mémoire: 22 tests

🔹 PRINTF — Tests de ft_printf- 🛡️ Validation — Sur-protection: 8 tests



📂 printf — Tests de ft_printf## 💡 Utilisation rapide

 [ 1/30] printf/basic_char ........................................ ✅ PASS (1 ms)

    printf():    Hello A```bash

    ft_printf(): Hello A# Lister tous les tests disponibles

..../tester.py /chemin/vers/libft --list

Résumé — 30/30 PASS

```# Exécuter tous les tests

./tester.py /chemin/vers/libft

## 🤝 Beta testeurs et support

# Exécuter une fonction spécifique

- Un grand merci aux beta testeurs qui ont aidé à stabiliser ce projet 🙌./tester.py /chemin/vers/libft --run strlen

- Issues: https://github.com/Blaeste/printferator/issues./tester.py /chemin/vers/libft --run memcpy

./tester.py /chemin/vers/libft --run list

---

# Mode verbeux (progression + logs complets)

<div align="center">./tester.py /chemin/vers/libft --verbose



⭐ Si ce projet vous aide, pensez à lui mettre une étoile ⭐# Désactiver les couleurs (pratique pour les logs CI)

./tester.py /chemin/vers/libft --no-color

[🏠 Accueil](https://github.com/Blaeste/printferator) • [🐛 Issues](https://github.com/Blaeste/printferator/issues)

# Mode sécurisé (aucune modif temporaire côté projet)

</div>./tester.py /chemin/vers/libft --safe
```

## 🧰 Options

- --list: affiche tous les tests disponibles et leur nom exécutable
- --run <nom>: exécute une sous-section (ex: strlen, memcpy, list)
- --verbose: affiche la progression détaillée et les logs complets
- --no-color: désactive les couleurs (utile pour la CI/logs)

## 🌟 Fonctionnalités avancées

### 🔍 Détection automatique des headers
- Recherche de `libft.h` dans `inc/`, `include/`, `includes/`, `headers/` et sous-dossiers
- Ajout automatique des `-I` nécessaires à la compilation
- Pas besoin de déplacer `libft.h` à la racine

### 🚰 Tests Valgrind intégrés
- Détection des fuites mémoire avec `--leak-check=full` et code retour d’erreur dédié
- Couverture spécifique: `calloc`, `strdup`, `substr`, `strjoin`, `strtrim`, `split`, `itoa`, `strmapi`, et fonctions bonus de listes
- Fallback gracieux si Valgrind est absent (les tests fonctionnent quand même)

### 🛡️ Tests de sur-protection
- Vérifie que certaines fonctions crashent sur `NULL` (comportement attendu par la libft)
- Section séparée des tests normaux pour une lecture claire

### 🎨 Interface lisible
- Affichage hiérarchique avec sous-sections par fonction (📂)
- Codes couleur: PASS ✅, FAIL ❌, LEAK 🚰
- Compteurs de progression et résumés en fin d’exécution

### 🧾 Système de logs
- Tous les résultats sont sauvegardés dans `out/` avec horodatage
- Logs norminette, compilation, exécution et métriques

### 🧩 Compatibilité
- Linux (recommandé) et WSL: support complet; Valgrind disponible via le gestionnaire de paquets
- macOS: fonctionnement OK; Valgrind n’est pas installé par défaut (fallback automatique)
- Windows natif: utilisez WSL pour une expérience optimale

### ❓ FAQ rapide
- Valgrind n’est pas installé ? Les tests s’exécutent quand même, mais sans détection de fuites (fallback). Installez-le via votre gestionnaire de paquets pour activer la section fuites mémoire.
- Où sont les logs ? Dans le dossier `out/`, avec un horodatage par session.
- Faut-il déplacer `libft.h` ? Non. Le testeur détecte automatiquement les répertoires d’en-têtes et ajoute les `-I`.

## 🖥️ Pré-requis

- Python 3.6+ (par défaut sur Linux des machines 42)
- Environnement POSIX (Linux/WSL conseillé). Valgrind est recommandé mais optionnel.

## 🧪 Exemple de sortie (extrait)

```
╔══════════════════════════════════════════════════════════════════╗
║                          Libfterator 2025                        ║
║                   281 tests • 5 sections • color                 ║
╚══════════════════════════════════════════════════════════════════╝

[norm] check ................................................ PASS
🔹 PARTIE 1 — Fonctions de la libc
	📂 strlen
	 [ 1/281] basic ......................................... PASS
	 [ 2/281] empty ......................................... PASS
...
Résumé — 281/281 PASS • 0 LEAK
```

## 🤝 Beta testeurs et support

- Un grand merci aux beta testeurs qui ont aidé à stabiliser ce projet 🙌
- Issues: https://github.com/Blaeste/libfterator/issues

---

<div align="center">

⭐ Si ce projet vous aide, pensez à lui mettre une étoile ⭐

[🏠 Accueil](https://github.com/Blaeste/libfterator) • [🐛 Issues](https://github.com/Blaeste/libfterator/issues)

</div>

