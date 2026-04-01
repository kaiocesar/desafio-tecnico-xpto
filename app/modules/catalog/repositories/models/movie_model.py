from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class MovieModel(Base):
    __tablename__ = 'movies'

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    title = Column(String, nullable=False)
    release_year = Column(String, nullable=False)

    producers = relationship(
        "ProducerModel",
        secondary="movie_producer",
        back_populates="movies"
    )

    studios = relationship(
        "StudioModel",
        secondary="movie_studio",
        back_populates="movies"
    )

    awards = relationship(
        "AwardModel",
        back_populates="movie"
    )