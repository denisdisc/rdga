from flask import Flask, flash, render_template, redirect, session, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.db import db
from webapp.events.models import Events
from webapp.admin.views import blueprint as admin_blueprint
from webapp.cont.views import blueprint as cont_blueprint
from webapp.user.models import User
from webapp.user.forms import LoginForm
from webapp.admin.forms import AddEventForm
from webapp.user.views import blueprint as user_blueprint
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(cont_blueprint)
    Breadcrumbs(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    @register_breadcrumb(app, '.', 'Главная')
    def index():
        if session is None:
            session["city"] = "no"
        page_title = "Диск-гольф Россия"
        return render_template('index.html', page_title=page_title)

    return app
