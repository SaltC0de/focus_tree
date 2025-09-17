from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate, UserRead
from deps import get_db
from security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session=Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    hashed = hash_password(payload.password)

    user = User(email=payload.email, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
























# router = APIRouter(prefix="/auth", tags=["auth"])

# @router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
# def register(payload: UserCreate, db: Session = Depends(get_db)):
#     existing = db.query(User).filter(User.email == payload.email).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Email is already registered")

#     hashed = hash_password(payload.password)

#     user = User(email=payload.email, password=hashed)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
