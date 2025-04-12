from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from dotenv import load_dotenv
import os


class UserBase(SQLModel):

    name : str = Field(unique=True)
    email: str | None = Field(unique=True)
    score: int = Field(default=0, ge=0, le=100) # zakres 0-100
    current_level: int = Field(default=1, ge=1, le=10) # minimum level 1, maks level 10

class User(UserBase, table=True):

    __tablename__ = "users"
    model_config = {"arbitrary_types_allowed": True}

    id: int = Field(primary_key=True)


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
