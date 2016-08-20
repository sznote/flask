from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#config
import os
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from models import * 

from project.users.views import users_blueprint

# register  our blueprints
app.register_blueprint(users_blueprint)
