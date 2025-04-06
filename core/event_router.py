from fastapi import APIRouter, HTTPException
from typing import List
from .database import EventBase, Event, SessionDep


router = APIRouter()

events = []
event_id_counter = 0


@router.get("/events/", response_model=List[Event])
def get_events():
    return events


@router.post("/events/", response_model=Event)
def create_event(event: EventBase, session: SessionDep):
    global event_id_counter
    new_event = Event(id=event_id_counter, **event.dict())
    events.append(new_event)

    # database
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    event_id_counter += 1
    return new_event


@router.get("/events/{event_id}", response_model=Event)
def get_event_by_id(event_id: int):
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")


@router.delete("/events/{event_id}", response_model=Event)
def delete_event(event_id: int):
    for i, event in enumerate(events):
        if event.id == event_id:
            return events.pop(i)
    raise HTTPException(status_code=404, detail="Event not found")
