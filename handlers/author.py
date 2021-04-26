import flask
from flask import render_template
from flask_login import current_user

from data import db_session
from data.news import News


blueprint = flask.Blueprint(
    'post',
    __name__,
    template_folder='templates'
)


@blueprint.route('/author/<int:id>')
def author(id):
    db_sess = db_session.create_session()

    news = db_sess.query(News).filter(News.user_id == id)
    user = {}

    for i in news:
        user['name'] = i.user.name
        user['about'] = i.user.about
        user['date'] = i.user.created_date
    return render_template('author.html', news=news, id=id, user=user)


@blueprint.route('/subscribe/<int:id>')
def sub(id):
    subs = []
    db_sess = db_session.create_session()
    users_subs = db_sess.query(News).filter(News.user == current_user)
    if id not in users_subs.subs:
        subs.append(id)
        users_subs.subs = id
        db_sess.commit()

    return render_template('author.html')