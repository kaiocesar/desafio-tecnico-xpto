from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE = "sqlite:///./movies.db"

engine = create_engine(DATABASE, connect_args={"check_same_thread": False}, poolclass=StaticPool)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()
