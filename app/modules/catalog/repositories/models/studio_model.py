from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class StudioModel(Base):
    __tablename__ = 'studios'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    movies = relationship("MovieModel", secondary="movie_studio", back_populates="studios")
