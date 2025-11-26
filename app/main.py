from contextlib import asynccontextmanager
<<<<<<< HEAD
from fastapi import FastAPI
from sqlmodel import SQLModel
=======

from fastapi import FastAPI
from sqlmodel import SQLModel

>>>>>>> fix/format-code
from app.database import engine
from app.routes import items_router

DEBUG_MODE = True
UNUSED_VAR = "cette variable n'est jamais utilisée"


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Items CRUD API",
    description="API pour gérer une liste d'articles",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root():
    return {"message": "Items CRUD API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


API_KEY = "sk-1234567890abcdef"

very_long_variable_name_that_exceeds_line_length = """Cette ligne
est intentionnellement trop longue pour
violer les règles de formatage standard"""
