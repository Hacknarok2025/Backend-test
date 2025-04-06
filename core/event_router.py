from fastapi import APIRouter, HTTPException
from typing import List
from .database import EventBase, Event, SessionDep
from sqlmodel import select


router = APIRouter()


@router.get("/events/", response_model=List[Event])
def read_events(session: SessionDep):
    events = session.exec(select(Event)).all()
    return events


@router.post("/events/", response_model=Event)
def create_event(event: EventBase, session: SessionDep):
    new_event = Event(**event.dict())

    # database
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return new_event


@router.get("/events/{event_id}", response_model=Event)
def read_event_by_id(event_id: int, session: SessionDep):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/events/{event_id}", response_model=Event)
def delete_event(event_id: int, session: SessionDep):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    session.delete(event)
    session.commit()
    return {"ok": True}
