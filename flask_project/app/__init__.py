# Flask app/db etc. config file

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import timedelta
from .constants import DB_PATH
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    encryptor = md5()
    app.permanent_session_lifetime = timedelta(minutes=30)
    app.secret_key = encryptor.digest()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    db.init_app(app)
    ma.init_app(app)

    app.debug = True

    from .main import main_blueprint, add_film_blueprint,show_all_blueprint,add_opinion_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(add_film_blueprint)
    app.register_blueprint(show_all_blueprint)
    app.register_blueprint(add_opinion_blueprint)

    return app