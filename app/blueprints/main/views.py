from app.blueprints.main.models import EmailModel
from app.blueprints.main.serializers import EmailSchema
from app.blueprints.main.utils import send_batch_mail_async
from app.blueprints.main.utils import send_mail_async
from app.extensions import db
from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request
from marshmallow import ValidationError


bp = Blueprint("main", __name__, url_prefix="/mail", template_folder="templates")


@bp.before_request
def check_headers():
    if request.headers.get("Accept") != "application/json":
        abort(406)
    if (
        request.method == "POST"
        and request.headers.get("Content-Type") != "application/json"
    ):
        abort(406)


@bp.route("/", methods=["POST"])
def send_new_mail():
    request_data = request.get_json()

    if not request_data:
        return (
            jsonify({"status": "error", "message": "Empty request body provided"}),
            400,
        )

    try:
        schema = EmailSchema()
        schema.load(request_data)

        send_mail_async(request_data)
        email = EmailModel(**request_data)

        db.session.add(email)
        db.session.commit()

        return jsonify({"status": "ok", "message": "Mail send successfully"}), 201
    except ValidationError:
        return jsonify({"status": "error", "message": "Invalid request schema"}), 400


@bp.route("/batch", methods=["POST"])
def send_batch_mail():
    request_data = request.get_json()

    if not request_data:
        return (
            jsonify({"status": "error", "message": "Empty request body provided"}),
            400,
        )

    try:
        schema = EmailSchema(many=True)
        schema.load(request_data)

        send_batch_mail_async(request_data)
        emails = [EmailModel(**data) for data in request_data]

        db.session.add_all(emails)
        db.session.commit()
    except ValidationError:
        return jsonify({"status": "error", "message": "Invalid request schema"}), 400

    return jsonify({"status": "ok", "message": "Hello world!!"}), 201
