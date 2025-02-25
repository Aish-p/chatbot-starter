from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.env import DATABASE_URL


engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
