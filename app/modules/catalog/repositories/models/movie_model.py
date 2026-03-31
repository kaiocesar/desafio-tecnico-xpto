from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql.base import UUID

from app.core.database import Base


class MovieModel(Base):
    __tablename__ = 'movies'

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(String, nullable=False)
