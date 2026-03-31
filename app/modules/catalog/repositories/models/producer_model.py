from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql.base import UUID

from app.core.database import Base


class ProducerModel(Base):
    __tablename__ = 'producer'

    id = Column(String, primary_key=True)
    name = Column(String)
