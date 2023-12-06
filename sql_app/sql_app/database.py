from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DB_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False} # check_same_thread is only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()