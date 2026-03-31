from sqlalchemy import Column, String, ForeignKey

from app.core.database import Base


class MovieStudioModel(Base):
    __tablename__ = "movie_studio"

    movie_id = Column(String, ForeignKey('movies.id'), nullable=False)
    studio_id = Column(String, ForeignKey('studio.id'), nullable=False)
