from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class AwardModel(Base):
    __tablename__ = 'awards'

    id = Column(String, primary_key=True)
    movie_id = Column(String, ForeignKey("movies.id"), nullable=False)
    year = Column(String, nullable=False)
    winner = Column(Boolean, nullable=False)

    movie = relationship("MovieModel", back_populates="awards")
