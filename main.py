# Про науку
from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.users import User
from data.news import News
from forms import login
from flask_login import LoginManager
from handlers import index, reqister, login, account, author, post, news_delete, edit_news, logout, \
    archive

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/like')
def like():
    print('like')
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(index.blueprint)
    app.register_blueprint(reqister.blueprint)
    app.register_blueprint(login.blueprint)
    app.register_blueprint(account.blueprint)
    app.register_blueprint(edit_news.blueprint)
    app.register_blueprint(news_delete.blueprint)
    app.register_blueprint(post.blueprint)
    app.register_blueprint(logout.blueprint)
    app.register_blueprint(author.blueprint)
    app.register_blueprint(archive.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()
