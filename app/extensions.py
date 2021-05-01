from flask_mailman import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
