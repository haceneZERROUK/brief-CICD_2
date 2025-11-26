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
