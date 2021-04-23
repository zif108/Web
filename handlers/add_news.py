import flask
from flask import render_template
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from data import db_session
from data.news import News
from forms.news import NewsForm

blueprint = flask.Blueprint(
    'add_news',
    __name__,
    template_folder='templates'
)


@blueprint.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.tag = form.tag.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('edit.html', title='Добавление новости',
                           form=form)
