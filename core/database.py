from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date, time
from dotenv import load_dotenv
import os


class EventBase(SQLModel):

    title: str
    description: str | None
    date: date
    start_time: time
    end_time: time


class Event(EventBase, table=True):

    __tablename__ = "events"
    model_config = {"arbitrary_types_allowed": True}

    id: int = Field(primary_key=True)


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

postgres_url = "postgresql://USER:PASSWORD@HOST:PORT/DATABASE"
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
