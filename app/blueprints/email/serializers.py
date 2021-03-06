from app.blueprints.email.models import EmailModel
from app.extensions import ma


class EmailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmailModel
