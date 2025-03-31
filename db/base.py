# app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Importa tus modelos aquí para que SQLAlchemy los reconozca
from models.persona import Persona  # noqa
