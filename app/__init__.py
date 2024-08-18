""" This module contains the necessary configs
to run the flask app """
from flask import Flask
from .models import db, User, Commodity, Orders
import secrets
from flask_migrate import Migrate
from flask_bootstrap5 import Bootstrap
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://shopper:shopvistashopper@localhost/shopvista'
    app.secret_key = secrets.token_urlsafe(16)

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap(app)
    csrf = CSRFProtect()
    csrf.init_app(app)

    with app.app_context():
        from .routes import register_routes
        register_routes(app)
#        db.create_all()

    return app
