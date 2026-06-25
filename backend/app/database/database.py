from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

#create database engine
engine = create_engine(DATABASE_URL)

#create session factory
SessionLocal = sessionmaker(
  autocommit = False,
  autoflush = False,
  bind = engine
)

Base = declarative_base()

def get_db():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()