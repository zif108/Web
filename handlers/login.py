import flask
from flask import render_template
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from data import db_session
from data.news import News
from data.users import User
from forms.login import LoginForm
from forms.user import RegisterForm

blueprint = flask.Blueprint(
    'login',
    __name__,
    template_folder='templates'
)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)
