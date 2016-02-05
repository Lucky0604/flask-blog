

' initial file '

__author__ = 'Lucky'

from flask import Flask
# 初始化应用程序的时候，我们也必须初始化数据库
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# read config.py
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models