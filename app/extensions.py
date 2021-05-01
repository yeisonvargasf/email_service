from flask_mailman import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
