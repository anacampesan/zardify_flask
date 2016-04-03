from main import app
from flask import render_template
from models import *

METHODS = ['GET', 'POST']

# getting the last song added
song = songWeek.query.order_by(songWeek.id.desc()).first()

@app.route('/')
def home():
    return render_template("home.html", title = "home", song = song)

@app.route('/music_reviews')
def music_reviews():
    return render_template("music_reviews.html", title = "music reviews")

@app.route('/other_stuff')
def other_stuff():
    return render_template("other_stuff.html", title = "other stuff")

@app.route('/about')
def about():
    return render_template("about.html", title = "about")

@app.route('/email')
def email():
    return render_template("email.html", title = "e-mail")