# from app import app

'''
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world"
'''

# add html
'''
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}       # fake user
    return
    <html>
        <head>
            <title>Home page</title>
        </head>
        <body>
            <h1>Hello, + user['nickname'] +  </h1>
        </body>
    </html>

'''

# use template
from flask import render_template, flash, redirect
from app import app
# add login form
from .forms import LoginForm

'''
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}       # fake user
    return render_template('index.html',
        title = 'Home',
        user = user)
'''

# add some info
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Lucky'}        # fake user
    posts = [
        {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland'
        },
        {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)