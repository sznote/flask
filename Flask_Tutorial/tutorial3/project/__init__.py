from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
 

from project.users.views import users_blueprint
from project.home.views import home_blueprint


# register  our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
