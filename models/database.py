from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_NAME = "sqlite3.db"

engine = create_engine(f"sqlite:///{DATABASE_NAME}", echo=True, future=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
