from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_repository(repository_class: Type):
    def _get_repo(db: Session = Depends(get_db)):
        return repository_class(db)
    return _get_repo
