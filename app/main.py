from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User

app = FastAPI(title="OnlyFlans API")


@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}


@app.get("/api/v1/users")
def get_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()

    return users
