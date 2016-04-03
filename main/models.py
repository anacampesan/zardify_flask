from main import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    
class songWeek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    artist = db.Column(db.String(80), unique=True)
    album = db.Column(db.String(80), unique=True)
    year = db.Column(db.String(80), unique=True)
    link = db.Column(db.String(80), unique=True)

    def __init__(self, title, artist, album, year, link):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.link = link

    def __repr__(self):
        return '<Song %r>' % self.title
    
