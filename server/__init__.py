from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from .apis.bulletin import BulletinAPI
from .apis.user import UserAPI, LoginAPI
from .db.model import db


def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    app.config['DEBUG'] = 'True'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
