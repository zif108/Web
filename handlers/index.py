import random

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
    news_with_tags = db_sess.query(News).filter(News.tag != None).all()
    while True:
        id_no_tag1 = random.randint(0, len(news_with_tags) - 1)
        id_no_tag2 = random.randint(0, len(news_with_tags) - 1)
        if id_no_tag1 != id_no_tag2:
            break
    tag1 = news_with_tags[id_no_tag1]
    tag2 = news_with_tags[id_no_tag2]
    # news1 = []
    # for i in news:
    #     i.title.replace('\n', )
    news1 = [i for i in news]
    news2 = news1[::-1]
    id_no = random.randint(0, len(news2) - 1)
    max_id = news2[id_no]

    if news_poisk != '':
        return render_template("mpage.html", news=news_poisk, max_new=max_id, tag1=tag1, tag2=tag2)

    else:
        return render_template("mpage.html", news=news2, max_new=max_id, tag1=tag1, tag2=tag2)
