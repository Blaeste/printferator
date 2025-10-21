# 🚀 Printferator 2025 - Tester Modulaire

[![Tests](https://img.shields.io/badge/Tests-30%2F30-brightgreen)](https://github.com/Blaeste/printferator)
[![Norminette](https://img.shields.io/badge/Norminette-100%25-blue)](https://github.com/42School/norminette)
[![42 School](https://img.shields.io/badge/42-School-000000)](https://42.fr)

> Testeur modulaire et facilement adaptable pour **ft_printf** et d'autres fonctions de l'École 42.


## ⚡ Installation ultra-rapide

```bash

git clone https://github.com/Blaeste/printferator.git

cd printferator./tester.py ./printf

```

# Tester avec des options

```bash./tester.py ./printf --verbose

./tester.py /chemin/vers/votre/printf./tester.py ./printf --run "basic"

# Exemple: ./tester.py ../printf./tester.py ./printf --list

``````

**C'est tout ! Aucune dépendance requise.**

Fonctionne avec Python 3.6+ (installé par défaut sur les machines 42).

---

### Pour ft_printf (par défaut)

## ✨ Points forts```python

- ✅ Norminette intégrée (vérification automatique)

- 🧪 30 tests exhaustifs avec cas limites et edge cases

- 🎨 Interface claire avec séparation printf() vs ft_printf()

- 🧾 Logs complets et métriques détaillées

- ⏱️ Timeout configurable pour éviter les boucles infinies


## 🎯 Couverture des tests (30)

- 📂 **printf** — Tests de ft_printf: 30 tests```

  - Formats de base: `%c`, `%s`, `%d`, `%i`, `%u`, `%x`, `%X`, `%p`, `%%`

  - Cas limites: `NULL`, valeurs maximales, chaînes vides### Pour toute la libft

  - Edge cases: pointeurs null, caractères spéciaux, formats complexes```python


## 💡 Utilisation rapide

### Lister tous les tests disponibles
```bash
./tester.py /chemin/vers/printf --list
```
### Exécuter tous les tests
```bash
./tester.py /chemin/vers/printfprintferator/
```
### Exécuter des tests spécifiques
```bash
./tester.py /chemin/vers/printf --run basic

./tester.py /chemin/vers/printf --run hex

./tester.py /chemin/vers/printf --run edge
```
### Mode verbeux (progression + logs complets)
```bash
./tester.py /chemin/vers/printf --verbose
```
### Désactiver les couleurs (pratique pour les logs CI)
```bash
./tester.py /chemin/vers/printf --no-color
```
### Timeout personnalisé
```bash
./tester.py /chemin/vers/printf --timeout 10
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

