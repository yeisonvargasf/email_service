from app.blueprints.email import email_bp
from app.blueprints.email.models import EmailModel  # noqa: F401
from app.blueprints.health import health_bp
from app.extensions import db
from app.extensions import ma
from app.extensions import mail
from app.extensions import migrate
from flask import Flask


def create_app(test_settings=None):
    app = Flask(__name__)

    app.config.from_object("config.settings")

    if test_settings:
        app.config.update(test_settings)

    app.logger.setLevel(app.config["LOG_LEVEL"])

    app.register_blueprint(health_bp)
    app.register_blueprint(email_bp)

    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app
