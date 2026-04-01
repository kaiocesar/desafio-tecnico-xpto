from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.core.database import Base


class ProducerModel(Base):
    __tablename__ = 'producers'

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)

    movies = relationship("MovieModel", secondary="movie_producer", back_populates="producers")
