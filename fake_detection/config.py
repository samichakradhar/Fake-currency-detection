# from decouple import config

class Config:
    SECRET_KEY = 'SECRET_KEY'
    # database name
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True