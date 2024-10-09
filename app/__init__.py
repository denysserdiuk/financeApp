from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)  # Load configuration from config.py
    db.init_app(app)  # Initialize SQLAlchemy with the app

    # Import and register routes
    from app.routes import user_routes
    from app.routes import web_routes

    app.register_blueprint(user_routes.bp)
    app.register_blueprint(web_routes.wp)

    return app