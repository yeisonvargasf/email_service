from app.extensions import ma
from app.blueprints.main.models import EmailModel


class EmailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmailModel
