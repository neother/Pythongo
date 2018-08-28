from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
import os

app = Flask(__name__)

bootstrap = Bootstrap()
db = SQLAlchemy()

'''
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
'''

moment = Moment()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    # ...

    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'hardtoguess'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .auth import auth as auth_blueprint
    from .auth import main as main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, url_prefix='/main')

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    # app.debug = True
    return app
