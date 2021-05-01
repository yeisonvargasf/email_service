from app.blueprints.main import main_bp
from app.blueprints.main.models import EmailModel  # noqa: F401
from app.extensions import db
from app.extensions import ma
from app.extensions import mail
from app.extensions import migrate
from flask import Flask
from flask import jsonify


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.settings")
    app.logger.setLevel(app.config["LOG_LEVEL"])

    app.register_blueprint(main_bp)

    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
