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
