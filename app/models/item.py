from sqlmodel import Field, SQLModel
<<<<<<< HEAD
=======

>>>>>>> fix/format-code

class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: int | None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    prix: float