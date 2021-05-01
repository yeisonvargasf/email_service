from flask_mailman import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
