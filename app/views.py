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
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
# add login form
from .forms import LoginForm
from .models import User

'''
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}       # fake user
    return render_template('index.html',
        title = 'Home',
        user = user)
'''
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

# add some info
@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'nickname': 'Lucky'}        # fake user
    user = g.user           # real user
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
@oid.loginhandler
def login():

    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    # 验证并且存储表单数据
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

    return render_template('login.html',
        title = 'Sign In',
        form = form,
        # 登录视图函数中使用OpenID 提供者的列表
        providers = app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login, Please try again')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False

    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)

    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
