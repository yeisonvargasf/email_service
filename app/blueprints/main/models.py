from sqlalchemy.dialects.postgresql import JSON

from app.extensions import db


class EmailModel(db.Model):
    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), index=True, nullable=False)
    template_id = db.Column(db.Integer)
    request_id = db.Column(db.String(32), index=True, nullable=False)
    template_params = db.Column(JSON)
