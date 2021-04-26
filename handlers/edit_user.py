import flask
from flask import render_template, request
from flask_login import login_required
from flask_restful import abort
from werkzeug.utils import redirect

from data import db_session
from data.users import User
from forms.user import RegisterForm

blueprint = flask.Blueprint(
    'edit_profile',
    __name__,
    template_folder='templates'
)


@blueprint.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = RegisterForm()
    print('asd')
    if request.method == "GET":
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()
        print(1)
        if user:
            form.name.data = user.name
            form.about.data = user.about
            form.email.data = user.email
            form.password.data = user.hashed_password
            form.password_again.data = user.hashed_password
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()
        print(2)
        if user:
            user.name = form.name.data
            user.about = form.about.data
            user.email = form.email.data
            user.password = form.password.data

            db_sess.commit()
            return redirect('/account')
        else:
            abort(404)
    return render_template('edit_user.html',
                           title='Редактирование профиля',
                           form=form
                           )
