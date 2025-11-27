models/item.py
nom du fichier
import inutile
la fonction _legacy_method ne fait rien

routes/items.py

import de datetime inutile
la class itemcreate est pas utilisé
l'import de List est pas utilisé

schemas/item.py
nom du fichier
import typing inutile
class itemcreate : vide et enfant de item base

services/item_service.py
docstrings trop longues

il y aussi des variables d'environnement qui sont dans les fichiers


>>>>>>>>>>><  erreurs Ruff :

F401 [*] `sys` imported but unused
  --> app/database.py:9:8
   |
 7 | from sqlmodel import create_engine, Session
 8 | import os
 9 | import sys
   |        ^^^
10 | from typing import Generator
   |
help: Remove unused import: `sys`

F401 [*] `typing.Generator` imported but unused
  --> app/database.py:10:20
   |
 8 | import os
 9 | import sys
10 | from typing import Generator
   |                    ^^^^^^^^^
11 |
12 | DATABASE_URL = os.getenv(
   |
help: Remove unused import: `typing.Generator`

F401 [*] `os` imported but unused
 --> app/main.py:2:8
  |
1 | from contextlib import asynccontextmanager
2 | import os
  |        ^^
3 | import sys
4 | from fastapi import FastAPI
  |
help: Remove unused import: `os`

F401 [*] `sys` imported but unused
 --> app/main.py:3:8
  |
1 | from contextlib import asynccontextmanager
2 | import os
3 | import sys
  |        ^^^
4 | from fastapi import FastAPI
5 | from sqlmodel import SQLModel
  |
help: Remove unused import: `sys`

F401 [*] `json` imported but unused
 --> app/main.py:6:8
  |
4 | from fastapi import FastAPI
5 | from sqlmodel import SQLModel
6 | import json
  |        ^^^^
7 | from typing import Dict, Any
8 | from app.database import engine
  |
help: Remove unused import: `json`

F401 [*] `typing.Dict` imported but unused
 --> app/main.py:7:20
  |
5 | from sqlmodel import SQLModel
6 | import json
7 | from typing import Dict, Any
  |                    ^^^^
8 | from app.database import engine
9 | from app.routes import items_router
  |
help: Remove unused import

F401 [*] `typing.Any` imported but unused
 --> app/main.py:7:26
  |
5 | from sqlmodel import SQLModel
6 | import json
7 | from typing import Dict, Any
  |                          ^^^
8 | from app.database import engine
9 | from app.routes import items_router
  |
help: Remove unused import

F401 [*] `typing.Optional` imported but unused
 --> app/models/item.py:2:20
  |
1 | from sqlmodel import Field, SQLModel
2 | from typing import Optional
  |                    ^^^^^^^^
3 |
4 | class Item(SQLModel, table=True):
  |
help: Remove unused import: `typing.Optional`

F401 [*] `typing.List` imported but unused
 --> app/routes/items.py:3:20
  |
1 | from fastapi import APIRouter, Depends, HTTPException, status
2 | from sqlmodel import Session
3 | from typing import List
  |                    ^^^^
4 | import datetime
  |
help: Remove unused import: `typing.List`

F401 [*] `datetime` imported but unused
 --> app/routes/items.py:4:8
  |
2 | from sqlmodel import Session
3 | from typing import List
4 | import datetime
  |        ^^^^^^^^
5 |
6 | from app.database import get_db
  |
help: Remove unused import: `datetime`

F401 [*] `app.schemas.item.ItemCreate` imported but unused
 --> app/routes/items.py:7:30
  |
6 | from app.database import get_db
7 | from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
  |                              ^^^^^^^^^^
8 | from app.services.item_service import ItemService
  |
help: Remove unused import: `app.schemas.item.ItemCreate`

F401 [*] `typing.Optional` imported but unused
 --> app/schemas/item.py:2:20
  |
1 | from sqlmodel import Field, SQLModel
2 | from typing import Optional
  |                    ^^^^^^^^
3 |
4 | class ItemBase(SQLModel):
  |
help: Remove unused import: `typing.Optional`

Found 12 errors.
[*] 12 fixable with the `--fix` option.

<<<<<<<<<<<<<<<<<MYPY>>>>>>>>>>>>>>>>>

app/database.py:19: error: Function is missing a return type annotation  [no-untyped-def]
app/models/item.py:10: error: Function is missing a return type annotation  [no-untyped-def]
app/models/item.py:10: note: Use "-> None" if function does not return a value
app/routes/items.py:13: error: Function is missing a return type annotation  [no-untyped-def]
app/routes/items.py:19: error: Function is missing a return type annotation  [no-untyped-def]
app/routes/items.py:19: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
app/routes/items.py:30: error: Function is missing a type annotation  [no-untyped-def]
app/routes/items.py:35: error: Function is missing a return type annotation  [no-untyped-def]
app/routes/items.py:46: error: Function is missing a return type annotation  [no-untyped-def]
app/routes/items.py:54: error: Function is missing a type annotation  [no-untyped-def]
app/main.py:12: error: Function is missing a return type annotation  [no-untyped-def]
app/main.py:28: error: Function is missing a return type annotation  [no-untyped-def]
app/main.py:33: error: Function is missing a return type annotation  [no-untyped-def]
Found 12 errors in 4 files (checked 11 source files)

### ❓ Questions de réflexion

1. **Le code fonctionne, mais** :
   - Est-il maintenable ?
   non car l'API fonctionne mais on ne peut pas alimenter la BDD, il y a encore plusieurs erreurs de linters, manque de typage

   - Est-il sécurisé ?
non il n'est pas sécurisé il y a plusieurs variables d'environnement qui sont mis en durs dans le code

   - Est-il bien documenté ?
Non le seul code qui est bien alimenté est item_services.py


2. **Comment détecter ces problèmes automatiquement ?**
   - Quels outils utiliser ?
   Les outils utilisés seront un Linter (ruff), un type check (mypy), un tester (pytest), et un security check (secrets)
   - À quel moment les exécuter ?
   il faut les exécuter à tous les moments de la pipeline CI/CD même en local lors du commit

3. **Comment empêcher ces problèmes à l'avenir ?**
signaler les erreurs au départ dès le commit afin de corriger les erreurs le plus tot possible.


### ❓ Questions de réflexion

1. **Pourquoi protéger les branches ?**
   - Que se passerait-il sans protection ?
   Sans les protections de branches, tous les membres du projet pourraient push dans la branche main et la develop. Sans que d'autres personnes puissent vérifier et ça aurait été push avec des erreurs potentiels. Ce qui peut mettre en péril le projet

2. **Pourquoi Conventional Commits ?**
   - Avantages pour l'équipe
ça rend plus lisible les commits et permet une standardisation qui permet de classer rapidement les commits

   - Avantages pour le versionnage automatique

Les Conventional Commits permettent le versionnage sémantique automatique (SemVer) :

Un commit fix: → incrémente le PATCH ​

Un commit feat: → incrémente le MINOR ​

Un commit avec BREAKING CHANGE: → incrémente le MAJOR

Des outils comme semantic-release ou standard-version lisent l'historique Git, déterminent automatiquement le numéro de version et génèrent le CHANGELOG sans intervention humaine. Cela évite les erreurs manuelles, accélère les releases et garantit la traçabilité (chaque version documente précisément ce qui a changé)


3. **Différence entre develop et main ?**
   - Quand merger dans develop ?
Dès qu'une feature branch est terminée et testée (feature/login vers develop).
   - Quand merger dans main ?
Quand merger ? Dès qu'une feature branch est terminée et testée (feature/login vers develop).


Voici les réponses structurées pour ton cours sur ces questions de réflexion CI/CD :

## Pourquoi plusieurs jobs séparés ?

### Avantages du parallélisme
- **Vitesse d'exécution :** Les jobs séparés s'exécutent en parallèle au lieu de s'exécuter l'un après l'autre. Si lint prend 2 min, tests 5 min et security 3 min, tout se termine en 5 min (le plus long) au lieu de 10 min (la somme).[1][2]
- **Utilisation optimale des ressources :** Chaque job tourne sur son propre runner, ce qui maximise l'utilisation du CPU/mémoire disponible sur GitHub Actions.[3][1]
- **Scalabilité :** Quand ton équipe grandit et pousse plus de code, tu peux augmenter le nombre de runners sans changer l'architecture du pipeline.[1]

### Facilité de débogage
- **Isolation des erreurs :** Si le job `security` échoue mais que `lint` et `tests` passent, tu sais exactement où chercher. Tu ne perds pas de temps à relire tous les logs.[4][5]
- **Relance ciblée :** GitHub Actions permet de relancer uniquement le job qui a échoué, pas tout le pipeline. Tu économises du temps et des crédits CI.[5]
- **Logs clairs :** Chaque job a son propre log séparé, facile à télécharger et analyser.[6][5]

## Que faire si la CI échoue ?

### Comment lire les logs ?
1. **Va dans l'onglet "Actions" sur GitHub** et clique sur le workflow qui a échoué.
2. **Clique sur le job rouge** (ex: `lint`, `tests`).
3. **Développe l'étape qui a échoué** (ex: "Exécuter ruff check").
4. **Lis le message d'erreur** de bas en haut : l'erreur principale est souvent à la fin.[5][6]

### Comment reproduire localement ?
```bash
# Avant de push, lance les mêmes commandes que le CI
uv run ruff check .
uv run mypy app/
uv run pytest --cov=app
```
Si ça passe localement, c'est que ton environnement local est aligné avec le CI. Si ça échoue, corrige avant de push.[6][5]

### Faut-il tout corriger d'un coup ?

**Non, jamais.** C'est la pire stratégie.

### Avantages des petites PR
- **Review plus rapide :** Les reviewers regardent une PR de 50 lignes en 10 minutes. Une PR de 500 lignes ? Ils procrastinent ou survolent.[7][8]
- **Moins de bugs :** Petite PR = petite surface d'attaque. Si un bug apparaît en prod, tu sais exactement quelle PR l'a introduit.[7]
- **Facilité de rollback :** Si une PR casse la prod, tu la revertes en 1 clic. Impossible avec une PR gigantesque qui touche 20 fichiers.[8][7]

### Facilité de review
- **Focus mental :** Un reviewer peut garder le contexte d'une petite feature en tête. Impossible avec une PR qui refactorise tout le projet.[8][7]
- **Feedback rapide :** Tu obtiens des retours en quelques heures, pas en plusieurs jours. Ça accélère ton cycle de développement.[7]
- **Moins de conflits :** Petites PR = mergées vite = moins de risque de conflits Git avec les autres devs.[7]

**La règle d'or :** Une PR = une branche = un problème corrigé. C'est pour ça que tu as créé des branches séparées (`fix/remove-unused-imports`, `fix/add-type-annotations`, etc.).

Voici les réponses structurées pour ton cours sur pre-commit vs CI :

## Différence entre pre-commit et CI ?

### Quand chacun s'exécute ?

**Pre-commit :**
- S'exécute **localement sur ta machine** au moment où tu tapes `git commit`
- Bloque le commit **avant** qu'il n'entre dans l'historique Git
- C'est le premier filet de sécurité, côté développeur

**CI (Continuous Integration) :**
- S'exécute **sur les serveurs GitHub Actions** après que tu aies push ton code
- Vérifie le code **après** qu'il soit entré dans l'historique et partagé
- C'est le second filet de sécurité, côté équipe

### Pourquoi avoir les deux ?

**Defense in Depth (défense en profondeur) :**
- **Pre-commit = feedback instantané (5-10 sec)** : Tu corriges immédiatement sans polluer l'historique Git avec des commits "fix typo" ou "oops forgot lint"
- **CI = vérification ultime (2-5 min)** : Garantit que même si quelqu'un bypass pre-commit, le code ne sera jamais mergé sans validation

**Protection contre le bypass :**
- Un développeur peut désactiver pre-commit localement, mais **il ne peut pas désactiver la CI sur GitHub**
- La CI est la vraie barrière avant le merge en production

## Peut-on bypass pre-commit ?

### `git commit --no-verify`

**Oui, c'est possible :**
```bash
git commit --no-verify -m "urgent fix"
# ou
git commit -n -m "bypass pre-commit"
```

### Est-ce une bonne idée ?

**Presque jamais.** Les seuls cas légitimes :
- Emergency hotfix en prod (incendie en cours)
- Pre-commit hook cassé temporairement (bug dans l'outil)
- Commit de fichiers générés automatiquement (ex: lockfiles)

**Mauvaises raisons (trop fréquentes) :**
- "Je suis pressé" → Tu perds plus de temps à attendre la CI échouer
- "Je corrigerai plus tard" → Tu ne corrigeras jamais
- "C'est juste un petit truc" → C'est toujours un "petit truc" qui casse la prod

### Comment l'empêcher ?

**Au niveau technique :**
- **Branch protection rules sur GitHub** : Impose que la CI passe avant merge, même si pre-commit a été bypass
- **CODEOWNERS + required reviews** : Force une revue humaine qui vérifie que le code respecte les standards

**Au niveau culturel :**
- Éduquer l'équipe : montrer que pre-commit fait gagner du temps, pas en perdre
- Lead by example : si les seniors bypass systématiquement, les juniors feront pareil

## Pre-commit ralentit-il le développement ?

### Temps d'exécution (5-10 secondes)

**C'est négligeable comparé aux alternatives :**

| Scénario | Sans pre-commit | Avec pre-commit |
|:---------|:----------------|:----------------|
| Commit local | 0.5 sec | 5-10 sec |
| Push + attente CI | 0 sec (tu push et tu zappes) | 0 sec (déjà validé) |
| CI échoue, tu découvres l'erreur | +3 min (CI) + 2 min (fix) + 3 min (re-CI) = **8 min** | **0 min** (erreur évitée) |
| Code review demande des changements de formatage | +1 jour (aller-retour reviewer) | **0 min** (auto-fixé) |

**Bilan :**
- Pre-commit ajoute 5-10 sec par commit
- Mais économise 8+ minutes à chaque fois qu'il détecte une erreur **avant** la CI
- Sur une journée avec 10 commits dont 2 auraient échoué en CI : **gain net de ~15 minutes**

### Vs temps perdu à attendre la CI

**Pre-commit = feedback loop court :**
- Tu commites → 10 sec → erreur trouvée → tu fixes → re-commit
- Total : **30 secondes** pour détecter + corriger

**Sans pre-commit :**
- Tu commites → tu push → 3 min de CI → erreur trouvée → tu fixes → tu push → 3 min de re-CI
- Total : **6+ minutes** pour le même résultat

**Conclusion pour ton cours :**
Pre-commit ne ralentit pas le développement, il **accélère la boucle de feedback** et réduit le coût cognitif (tu restes dans le même contexte mental au lieu de revenir 5 minutes plus tard sur un problème).


## Pourquoi containeriser ?

**Cohérence entre environnements** : Élimine le problème "ça marche sur ma machine" en empaquetant l'application avec toutes ses dépendances. Même comportement en développement, test et production.

**Portabilité totale** : Un conteneur fonctionne partout sans modification, que ce soit sur votre laptop, un serveur on-premise ou différents clouds. Vous pouvez changer de fournisseur cloud facilement.

**Déploiement rapide** : Les conteneurs démarrent en secondes contre plusieurs minutes pour les VM. Permet des mises à jour et rollbacks quasi-instantanés.

**Optimisation des ressources** : Plus légers que les VM car ils partagent le noyau de l'OS hôte. Vous pouvez lancer 2 à 3 fois plus de conteneurs que de VM sur le même hardware.

**Isolation des applications** : Chaque conteneur est indépendant. Une erreur dans un conteneur n'affecte pas les autres. Vous pouvez faire tourner des versions incompatibles de logiciels sur la même machine.

## Multi-stage build : pourquoi ?

**Taille de l'image** : Réduit la taille de 40 à 60%. Les outils de compilation comme gcc, npm ou Maven ne sont présents que pendant le build, pas dans l'image finale. Résultat : téléchargements plus rapides, moins d'espace disque.

**Sécurité** : Surface d'attaque réduite. En ne gardant que le strict nécessaire à l'exécution, vous éliminez les outils de développement qui pourraient contenir des vulnérabilités. Moins de packages = moins de failles potentielles.

## Tagging strategy

**Pourquoi plusieurs tags ?**

Flexibilité : Permet de cibler précisément la version souhaitée selon le contexte (dev, staging, production). Offre différents niveaux de stabilité.

Traçabilité : Retrouver l'image exacte d'un commit ou d'une version. Facilite les audits et le debugging.

Rollback : Revenir rapidement à une version spécifique en cas de problème.

**latest** : Pointe toujours vers le dernier build. Pratique pour le développement mais dangereux en production car non-déterministe. On ne sait jamais quelle version exacte on va obtenir.

**semver (v1.2.3)** : Versioning sémantique strict. Idéal pour la production car il garantit une version figée et prévisible. Permet de gérer les montées de version mineures vs majeures.

**sha (sha-abc1234)** : Lié directement au commit Git. Traçabilité parfaite et reproductibilité garantie. Utile pour les audits de sécurité et les déploiements critiques où il faut savoir exactement quel code tourne.
