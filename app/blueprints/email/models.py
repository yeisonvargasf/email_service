from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON


class EmailModel(db.Model):
    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), index=True, nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    template_id = db.Column(db.Integer)
    request_id = db.Column(db.String(32), index=True, nullable=False)
    template_params = db.Column(JSON)

    @classmethod
    def insert(cls, params):
        email = EmailModel(**params)

        db.session.add(email)
        db.session.commit()

    @classmethod
    def bulk_insert(cls, params):
        emails = [EmailModel(**param) for param in params]

        db.session.add_all(emails)
        db.session.commit()
