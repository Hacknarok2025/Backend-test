from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from dotenv import load_dotenv
import os
from passlib.context import CryptContext

# password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserBase(SQLModel):
    name: str = Field(unique=True)
    email: str | None = Field(default=None)


class User(UserBase, table=True):
    __tablename__ = "users"
    model_config = {"arbitrary_types_allowed": True}

    id: int = Field(primary_key=True, default=None)
    hashed_password: str = Field(default=None)
    score: int = Field(default=0, ge=0, le=1000)
    current_level: int = Field(default=1, ge=1, le=9)


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    score: int
    current_level: int


class LevelCompletion(SQLModel):
    score: int


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


SessionDep = Annotated[Session, Depends(get_session)]



    