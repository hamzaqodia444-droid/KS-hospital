from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


DATABASE_PATH = os.path.join(
    BASE_DIR,
    "..",
    "database",
    "hospital.db"
)


DATABASE_URL = "sqlite:///" + os.path.abspath(DATABASE_PATH)



engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()



def get_database():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
