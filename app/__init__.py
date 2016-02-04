

' initial file '

__author__ = 'Lucky'

from flask import Flask

app = Flask(__name__)
# read config.py
app.config.from_object('config')

from app import views