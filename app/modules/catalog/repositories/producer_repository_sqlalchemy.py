from sqlalchemy.orm import Session

from app.modules.catalog.repositories.interfaces.producer_interface import IProducerInterface


class ProducerRepositorySQLAlchemyRepository(IProducerInterface):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: str):
        return self.db.query().filter()

    def find_all(self):
        return self.db.find_all()
