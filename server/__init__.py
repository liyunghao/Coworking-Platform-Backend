from flask import Flask

def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    app.config['DEBUG'] = 'True'
    return app
