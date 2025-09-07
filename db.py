from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DB_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()