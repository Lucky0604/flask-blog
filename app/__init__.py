

' initial file '

__author__ = 'Lucky'

import os
from flask import Flask
# 初始化应用程序的时候，我们也必须初始化数据库
from flask.ext.sqlalchemy import SQLAlchemy


# For the login system we will use two extensions, Flask-Login and Flask-OpenID

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
# read config.py


from app import views, models
