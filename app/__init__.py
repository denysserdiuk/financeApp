from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from config.py
    db.init_app(app)  # Initialize SQLAlchemy with the app

    # Import and register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app