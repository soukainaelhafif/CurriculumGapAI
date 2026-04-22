from sqlalchemy import create_engine, Column, Integer, String, ARRAY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://soukainaelhafif@localhost/curriculumgapai")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Analyse(Base):
    __tablename__ = "analysen"
    
    id = Column(Integer, primary_key=True)
    datei_name = Column(String)
    fehlende_skills = Column(ARRAY(String))
    vorhandene_skills = Column(ARRAY(String))
    erstellt_am = Column(DateTime, default=datetime.now)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()