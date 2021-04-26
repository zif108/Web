import flask
from flask_login import current_user, login_required
from flask_restful import abort
from werkzeug.utils import redirect

from data import db_session
from data.news import News


blueprint = flask.Blueprint(
    'delete_news',
    __name__,
    template_folder='templates'
)


@blueprint.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')