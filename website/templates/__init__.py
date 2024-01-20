from flask import flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'slime slime'

    return app