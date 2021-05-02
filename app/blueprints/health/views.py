from flask import Blueprint
from flask import jsonify


bp = Blueprint("health", __name__, url_prefix="/health")


@bp.route("/")
def health_check():
    return jsonify({"status": "ok"}), 200
