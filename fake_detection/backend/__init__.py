from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  

app = Flask(__name__)
app.config.from_object(Config)

from fake_detection.backend.routes.login import login
from fake_detection.backend.routes.signup import signup
from fake_detection.backend.routes.user import get_all_users