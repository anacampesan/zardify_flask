from main import app
from flask import render_template
from models import *
import api

METHODS = ['GET', 'POST']

@app.route('/')
def home():
    return render_template("home.html", title = "home", 
                                        song = api.song_week())

@app.route('/music_reviews')
def music_reviews():
    return render_template("music_reviews.html", title = "music reviews", 
                                                 song = api.song_week(),
                                                 posts = api.posts(0))

@app.route('/other_stuff')
def other_stuff():
    return render_template("other_stuff.html", title = "other stuff", 
                                               song = api.song_week())

@app.route('/about')
def about():
    return render_template("about.html", title = "about",
                                         song = api.song_week())

@app.route('/email')
def email():
    return render_template("email.html", title = "e-mail",
                                         song = api.song_week())
