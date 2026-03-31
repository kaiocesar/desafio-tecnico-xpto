from sqlalchemy import Column, String, ForeignKey

from app.core.database import Base


class MovieStudioModel(Base):
    __tablename__ = "movie_studio"

    movie_id = Column(String, ForeignKey('movies.id'), nullable=False, primary_key=True)
    studio_id = Column(String, ForeignKey('studios.id'), nullable=False, primary_key=True)
