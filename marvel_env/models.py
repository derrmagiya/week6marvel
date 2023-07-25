from datetime import datetime
from marvel_api import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    characters = db.relationship('MarvelCharacter', backref='user', lazy=True)

class MarvelCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    comics_appeared_in = db.Column(db.Integer, nullable=False)
    super_power = db.Column(db.String(100), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_token = db.Column(db.String(255), db.ForeignKey('user.token'), nullable=False)