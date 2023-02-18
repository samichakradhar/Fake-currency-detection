from flask_sqlalchemy import SQLAlchemy
from fake_detection.backend import app
from datetime import datetime
from sqlalchemy import ForeignKey

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(80))
    

class Banknote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(70), unique = True)
    isReal = db.Column(db.Boolean)
    user_detail_id = db.Column(db.Integer,ForeignKey('user.id'))
    created_date = db.Column(db.DateTime, default = datetime.utcnow())

class IsReal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(70), unique = True)
    isRealCount = db.Column(db.Integer)
    user_detail_id = db.Column(db.Integer,ForeignKey('user.id'))
    