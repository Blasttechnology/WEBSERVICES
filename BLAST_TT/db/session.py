# db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Crea el engine con la URL proporcionada (asegurate de tener instalado psycopg2-binary)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
