import flask
from flask import render_template, request
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
        news_poisk = ''
        db_sess = db_session.create_session()
        q = request.args.get('q')
        if q:
            news_poisk = db_sess.query(News).filter(
                News.title.contains(q) | News.content.contains(q) | News.tag.contains(q)).all()
        # else:
        #     news = db_sess.query(News).filter(News.is_private != True)

        news = db_sess.query(News).filter(News.user == current_user).all()
        news = news[::-1]
        user = {}
        user['name'] = current_user.name
        user['about'] = current_user.about
        user['date'] = current_user.created_date
        user['id'] = current_user.id
        if news_poisk != '':
            return render_template('account.html', news=news_poisk, user=user)
        else:
            return render_template('account.html', news=news, user=user)