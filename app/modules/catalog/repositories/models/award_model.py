from sqlalchemy import Column, String, Boolean
from app.core.database import Base


class AwardModel(Base):
    __tablename__ = 'awards'

    id = Column(String, primary_key=True)
    year = Column(String, nullable=False)
    winner = Column(Boolean, nullable=False)
