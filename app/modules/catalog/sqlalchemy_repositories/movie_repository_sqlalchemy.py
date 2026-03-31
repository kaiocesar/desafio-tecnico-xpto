from sqlalchemy.orm import Session

from app.modules.catalog.repositories.interfaces.movie_interface import IMovieInterface


class MovieRepositorySQLAlchemyRepository(IMovieInterface):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, id: str):
        return self.db.query().filter()

    def find_all(self):
        return self.db.find_all()
