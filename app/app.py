from flask import Flask
from flask import jsonify

from app.extensions import mail
from app.blueprints.main import main_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.settings")
    app.logger.setLevel(app.config["LOG_LEVEL"])

    app.register_blueprint(main_bp)

    mail.init_app(app)

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app