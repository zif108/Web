import flask
from flask import render_template

from data import db_session
from data.news import News

blueprint = flask.Blueprint(
    'archive',
    __name__,
    template_folder='templates'
)


@blueprint.route('/archive/<string:str>')
def archive(str):
    db_sess = db_session.create_session()

    news = db_sess.query(News)

    corr = []
    for i in news:
        if i.created_date.month == int(str[:str.index('-')]):
            corr.append(i)
    return render_template('archive.html', news=corr)
