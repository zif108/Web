import flask
from flask import render_template
from flask_login import current_user
from werkzeug.utils import redirect

from data import db_session
from data.news import News
from data.users import User
from forms.user import RegisterForm

blueprint = flask.Blueprint(
    'tags',
    __name__,
    template_folder='templates'
)


@blueprint.route('/tags')
def tags():
    db_sess = db_session.create_session()
    tags = db_sess.query(News.tag)
    tags1 = []
    for i in tags:
        if i[0] is not None:
            tags1.append(i)
    tags2 = sorted(list(set(tags1)))
    return render_template('tag.html', tags=tags2)


@blueprint.route('/tags/<string:str>')
def news_tags(str):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.tag == str)
    return render_template('news_tags.html', news=news, str=str)
