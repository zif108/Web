import flask
from flask_login import login_required, logout_user
from werkzeug.utils import redirect

blueprint = flask.Blueprint(
    'logout',
    __name__,
    template_folder='templates'
)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
