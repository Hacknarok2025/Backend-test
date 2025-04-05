from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class Event(EventBase):
    id: int