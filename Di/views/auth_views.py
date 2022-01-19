from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from Di import db
from Di.forms import UserCreateForm, UserLoginForm
from Di.models import User

import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.mainpage'))
        else:
            flash('You already signed.')
    return render_template('auth/signup.html', form=form)

@bp.route('/signin/', methods=('GET', 'POST'))
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "It is not your name."
        elif not check_password_hash(user.password, form.password.data):
            error = "It is not your password."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.mainpage'))
        flash(error)
    return render_template('auth/signin.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/signout/')
def signout():
    session.clear()
    return redirect(url_for('main.mainpage'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.signin'))
        return view(**kwargs)
    return wrapped_view