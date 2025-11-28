# Items API Project

API REST développée avec **FastAPI** et **PostgreSQL**, intégrant une pipeline CI/CD complète et automatisée, respectant les pratiques DevOps modernes (Docker, Semantic Release, GitHub Actions).

## 🛠 Stack Technique

*   **Langage** : Python 3.13
*   **Framework** : FastAPI
*   **ORM** : SQLModel
*   **Base de données** : PostgreSQL
*   **Gestionnaire de paquets** : `uv` (Astral)
*   **Conteneurisation** : Docker (Multi-stage build)

## 🚀 Fonctionnalités CI/CD

Ce projet dispose d'une pipeline d'intégration et de déploiement continu (GitHub Actions) robuste :

### 1. Intégration Continue (CI)
Déclenchée à chaque `push` et `pull_request`.
*   **Qualité de code** : `ruff` (Linter & Formatter)
*   **Typage** : `mypy`
*   **Sécurité** : `bandit` (Analyse statique), `safety` (Dépendances vulnérables)
*   **Tests** : `pytest` avec rapport de couverture (Codecov)

### 2. Versioning Automatique (Semantic Release)
*   Déclenché automatiquement après la réussite de la CI sur les branches `develop` et `main`.
*   **Analyse des commits** : Utilise la convention Angular (`feat:`, `fix:`, `chore:`) pour déterminer le numéro de version.
*   **Génération automatique** :
    *   Bump de version (ex: `1.0.0` -> `1.1.0`)
    *   Création de Tag Git
    *   Génération du `CHANGELOG.md`
    *   Création d'une GitHub Release

### 3. Déploiement Continu (CD)
*   **Build Docker** : Construction optimisée de l'image.
*   **Registry** : Push automatique de l'image sur **GHCR** (GitHub Container Registry).
*   **Tagging** : L'image est taguée avec la version sémantique (ex: `v1.0.0`) et `latest`.

## 📦 Installation et Lancement

### Prérequis
*   Docker & Docker Compose
*   `uv` (optionnel, pour le dev local)

### Lancer avec Docker (Recommandé)
```
# Construire et lancer l'API et la BDD
docker compose up --build -d

# L'API sera accessible sur http://localhost:8000
# Documentation Swagger : http://localhost:8000/docs
```

### Développement Local
```
# 1. Installer les dépendances
uv sync

# 2. Lancer la BDD (via Docker)
docker run -d --name db_pg -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=items_db -p 5432:5432 postgres:16-alpine

# 3. Lancer l'API
uv run fastapi dev app/main.py
```

## 🔄 Workflow Git & Contribution

Nous utilisons le **GitHub Flow** adapté avec une branche `develop` protégée.

1.  **Créer une branche** pour votre fonctionnalité :
    ```
    git checkout -b feat/ma-nouvelle-feature
    ```
2.  **Commiter** en respectant les **Conventional Commits** (CRUCIAL pour le versioning) :
    *   `feat: ajout de la route login` (Crée une version Mineure)
    *   `fix: correction du crash database` (Crée une version Patch)
    *   `chore: mise à jour du readme` (Pas de release)
    ```
    git commit -m "feat: ajout de la route login"
    ```
3.  **Pousser et ouvrir une Pull Request** vers `develop`.
4.  Une fois la PR validée et mergée, la CI/CD prend le relais pour tester et publier.

## 🛡 Protection de Branches
*   **main** : Production (Versions stables).
*   **develop** : Intégration (Versions Release Candidate `rc`).
*   Les pushs directs sur `develop` sont interdits (sauf Admin/Bot), tout doit passer par une PR.

## 🐳 Docker Registry
L'image est disponible sur GHCR :
```
docker pull ghcr.io/hacenezerrouk/brief-cicd_2:latest
```
```
