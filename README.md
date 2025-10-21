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

## ✨ Points forts

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

- --list: affiche tous les tests disponibles et leur nom exécutable
- --run <nom>: exécute une sous-section (ex: strlen, memcpy, list)
- --verbose: affiche la progression détaillée et les logs complets
- --no-color: désactive les couleurs (utile pour la CI/logs)

## 🎨 Interface lisible
- Affichage hiérarchique avec sous-sections par fonction (📂)
- Codes couleur: PASS ✅, FAIL ❌, LEAK 🚰
- Compteurs de progression et résumés en fin d’exécution

## 🧾 Système de logs
- Tous les résultats sont sauvegardés dans `out/` avec horodatage
- Logs norminette, compilation, exécution et métriques

## 🧩 Compatibilité
- Linux (recommandé) et WSL: support complet; Valgrind disponible via le gestionnaire de paquets
- macOS: fonctionnement OK; Valgrind n’est pas installé par défaut (fallback automatique)
- Windows natif: utilisez WSL pour une expérience optimale

## 🖥️ Pré-requis

- Python 3.6+ (par défaut sur Linux des machines 42)
- Environnement POSIX (Linux/WSL conseillé). Valgrind est recommandé mais optionnel.

## 🤝 Beta testeurs et support

- Un grand merci aux beta testeurs qui ont aidé à stabiliser ce projet 🙌
- Issues: https://github.com/Blaeste/printferator/issues

---

<div align="center">

⭐ Si ce projet vous aide, pensez à lui mettre une étoile ⭐

[🏠 Accueil](https://github.com/Blaeste/printferator) • [🐛 Issues](https://github.com/Blaeste/printferator/issues)

</div>

