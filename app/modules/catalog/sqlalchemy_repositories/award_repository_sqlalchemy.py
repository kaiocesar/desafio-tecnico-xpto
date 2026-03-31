from sqlalchemy.orm import Session

from app.modules.catalog.repositories.interfaces.award_interface import IAwardInterface
from app.modules.catalog.repositories.models.award_model import AwardModel


class AwardRepositorySQLAlchemy(IAwardInterface):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: str):
        return self.db.query(AwardModel).filter(AwardModel.id == id).first()

    def find_all(self):
        return self.db.query(AwardModel).all()
