# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Paras%401123@localhost:5433/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
