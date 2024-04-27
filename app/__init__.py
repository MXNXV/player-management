from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import db  # Make sure this import is correct

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Verify this points to your config settings

    db.init_app(app)  # Initializes the SQLAlchemy instance with app

    with app.app_context():
        from .routes.player_routes import player_bp
        db.create_all()  # This creates all tables
        app.register_blueprint(player_bp, url_prefix='')

    return app
