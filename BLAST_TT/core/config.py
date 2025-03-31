# core/config.py
from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Carga explícita del archivo "archivo.env"
load_dotenv("archivo.env")

class Settings(BaseSettings):
    PROJECT_NAME: str = "ABM con FastAPI y PostgreSQL (Neon)"
    DATABASE_URL: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return self.DATABASE_URL

    class Config:
        # Indicamos que use "archivo.env" en lugar de ".env"
        env_file = "archivo.env"

settings = Settings()
