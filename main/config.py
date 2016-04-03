import os

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/zardify.sqlite3' % (os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False