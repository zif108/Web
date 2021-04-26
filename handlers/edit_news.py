import flask
from flask import render_template, request
from flask_login import current_user, login_required
from flask_restful import abort
from werkzeug.utils import redirect

from data import db_session
from data.news import News
from forms.news import NewsForm

blueprint = flask.Blueprint(
    'edit_news',
    __name__,
    template_folder='templates'
)


@blueprint.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.tag.data = news.tag
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.tag = form.tag.data
            news.content = form.content.data

            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('edit.html',
                           title='Редактирование новости',
                           form=form
                           )
