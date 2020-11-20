import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Basic configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()
