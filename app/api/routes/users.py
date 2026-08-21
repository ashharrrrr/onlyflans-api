from fastapi import APIRouter, Depends, status

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()

    return users


@router.post(
    "", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=user_data.username,
        email=user_data.email,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
