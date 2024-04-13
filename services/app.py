import os

from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import URL


def create_app():
    app = Flask(__name__)

    url_object = URL.create(
        "postgresql+psycopg",
        username="postgres",
        password=os.environ.get("DB_PASSWORD", "postgres"),
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "example"),
        port=os.environ.get("DB_PORT", 5432),
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = url_object

    from models.db import db

    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()

    from .views import views

    app.register_blueprint(views)

    return app
