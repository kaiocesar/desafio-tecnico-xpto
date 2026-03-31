from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class ProducerModel(Base):
    __tablename__ = 'producers'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    movies = relationship("MovieModel", secondary="movie_producer", back_populates="producers")
