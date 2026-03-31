from sqlalchemy import Column, String, ForeignKey

from app.core.database import Base


class MovieProducerModel(Base):
    __tablename__ = "movie_producer"

    movie_id = Column(String, ForeignKey('movies.id'), nullable=False)
    producer_id = Column(String, ForeignKey('producer.id'), nullable=False)
