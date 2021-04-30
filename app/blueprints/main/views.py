from flask import Blueprint, jsonify


bp = Blueprint("main", __name__, url_prefix="/mail")


@bp.route("/")
def list_all_mails():
    return jsonify({"status": "ok", "message": "Hello world!!"}), 200


@bp.route("/<string:mail_id>")
def get_single_mail(mail_id):
    return jsonify({"status": "ok", "message": "Hello world!!"}), 200


@bp.route("/", methods=["POST"])
def send_new_mail():
    return jsonify({"status": "ok", "message": "Hello world!!"}), 201


@bp.route("/batch", methods=["POST"])
def send_batch_mail():
    return jsonify({"status": "ok", "message": "Hello world!!"}), 200
