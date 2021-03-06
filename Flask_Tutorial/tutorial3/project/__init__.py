from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config.DevelopmentConfig')
#app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
 

from project.users.views import users_blueprint
from project.home.views import home_blueprint





# register  our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

#
from models  import User
login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
	return  User.query.filter(User.id == int(user_id)).first()