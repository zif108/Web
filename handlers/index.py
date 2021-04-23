import flask
from flask import render_template, request
from flask_login import current_user

from data import db_session
from data.news import News

blueprint = flask.Blueprint(
    'index',
    __name__,
    template_folder='templates'
)


@blueprint.route('/')
def index():
    news_poisk = ''
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    q = request.args.get('q')
    if q:
        news_poisk = db_sess.query(News).filter(
            News.title.contains(q) | News.content.contains(q) | News.tag.contains(q)).all()
    else:
        news = db_sess.query(News).filter(News.is_private != True)

    news1 = [i for i in news]
    news2 = news1[::-1]
    max_id = 0
    for i in range(len(news1)):
        if i == 0:
            max_id = news[i]
        else:
            if len(news[i].content) > len(news[i - 1].content):
                max_id = news[i]
    print(max_id)
    if news_poisk != '':
        return render_template("mpage.html", news=news_poisk, max_new=max_id)

    else:
        return render_template("mpage.html", news=news2, max_new=max_id)
