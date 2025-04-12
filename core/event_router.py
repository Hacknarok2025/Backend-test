from fastapi import APIRouter, HTTPException
from typing import List
from .database import (User, 
                       UserResponse, 
                       UserCreate, 
                       LevelCompletion, 
                       get_password_hash,
                       verify_password,
                       SessionDep
                       )
from sqlmodel import select


router = APIRouter()


@router.post("/users/login", response_model=UserResponse)
def login_user(user: UserCreate, session: SessionDep):
    db_user = session.exec(select(User).where(User.name == user.name)).first()
    
    
    if not db_user:
        hashed_password = get_password_hash(user.password)
        new_user = User(
            name=user.name,
            email=user.email,
            hashed_password=hashed_password,
            score=0, 
            current_level=1
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    else:
        if not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        return db_user

@router.get("/users/{user_id}")
def get_available_users(user_id: int, session:SessionDep):
     user = session.get(User, user_id)
     if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")
     
     return user


@router.get("/users/{user_id}/levels")
def get_available_levels(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")
    
    levels = []
    for i in range(1, 10): 
        levels.append({
            "level_id": i,
            "name": f"Poziom {i}",
            "unlocked": i <= user.current_level,
            "completed": i < user.current_level
        })
    
    return levels


@router.get("/levels/{level_id}/start")
def start_level(level_id: int, user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")
    
    if level_id > user.current_level:
        raise HTTPException(status_code=403, detail="Ten poziom jest jeszcze zablokowany")
    
    return {
        "level_id": level_id,
        "name": f"Poziom {level_id}",
        "description": f"Witaj w świecie nordyckim {level_id}"
    }


@router.post("/levels/{level_id}/complete")
def complete_level(
    level_id: int, 
    completion: LevelCompletion, 
    user_id: int, 
    session: SessionDep
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie istnieje")
    
    if level_id > user.current_level:
        raise HTTPException(status_code=403, detail="Ten poziom jest jeszcze zablokowany")
    
    if level_id == user.current_level and user.current_level < 9:
        user.current_level += 1
    
    user.score += completion.score
    if user.score > 100:
        user.score = 100  # Limit 100 punktów
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {
        "success": True,
        "next_level": user.current_level,
        "total_score": user.score,
        "message": "Poziom ukończony!"
    }


@router.get("/leaderboard", response_model=List[UserResponse])
def get_leaderboard(session: SessionDep):
    users = session.exec(select(User).order_by(User.score.desc()).limit(10)).all()
    return users