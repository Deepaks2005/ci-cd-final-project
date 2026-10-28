import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URI", "sqlite:///capstone.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from service.routes import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
