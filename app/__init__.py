

' initial file '

__author__ = 'Lucky'

import os
from flask import Flask
# 初始化应用程序的时候，我们也必须初始化数据库
from flask.ext.sqlalchemy import SQLAlchemy
# setting up an email when there is an exception is pretty easy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD


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

if not app.config:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_hanlder = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_hanlder.setLevel(logging.ERROR)
    app.logger.addHandler(mail_hanlder)


from app import views, models
