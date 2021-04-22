import flask
from flask import render_template
from flask_login import current_user

from data import db_session
from data.news import News

blueprint = flask.Blueprint(
    'account',
    __name__,
    template_folder='templates'
)


@blueprint.route('/account')
def acc():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.user == current_user)
        user = {}
        user['name'] = current_user.name
        user['about'] = current_user.about
        user['date'] = current_user.created_date
        return render_template('account.html', news=news, user=user)
