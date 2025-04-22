from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base

db = SQLAlchemy(model_class=Base) # instance of SQLAlchemy, pass in Base
# we'll use db to interact with the database (create/update, etc.)
migrate = Migrate()