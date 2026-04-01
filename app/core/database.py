from pathlib import Path

from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, declarative_base


PROJECT_ROOT = Path(__file__).parent.parent.parent
DATABASE_PATH = PROJECT_ROOT / "movies.db"
DATABASE = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE, connect_args={"check_same_thread": False}, poolclass=StaticPool)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()

def init_db():
    from app.modules.catalog.repositories.models.movie_model import MovieModel
    from app.modules.catalog.repositories.models.producer_model import ProducerModel
    from app.modules.catalog.repositories.models.studio_model import StudioModel
    from app.modules.catalog.repositories.models.movie_producer_model import MovieProducerModel
    from app.modules.catalog.repositories.models.movie_studio_model import MovieStudioModel

    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()