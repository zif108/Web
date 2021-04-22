import flask
from flask import render_template
from flask_login import login_required

from data import db_session
from data.news import News


blueprint = flask.Blueprint(
    'post_',
    __name__,
    template_folder='templates'
)


@blueprint.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id).first()
    href = f'/author/{news.user.id}'
    return render_template('post.html', news=news, href=href)
