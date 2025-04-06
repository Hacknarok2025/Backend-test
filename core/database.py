from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date, time


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


sql_file_name = "database.db"
sqlite_url = f"sqlite:///{sql_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
