from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: str
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time

class Event(EventBase):
    id: int