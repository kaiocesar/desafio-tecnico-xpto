from sqlalchemy.orm import Session

from app.modules.catalog.repositories.interfaces.studio_interface import IStudioInterface


class ProducerRepositorySQLAlchemyRepository(IStudioInterface):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: str):
        return self.db.query().filter()

    def find_all(self):
        return self.db.find_all()
