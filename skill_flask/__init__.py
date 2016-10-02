from flask import Flask 
from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)


app.config['SECRET_KEY'] = "Hello saza"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bcrypt  = Bcrypt(app)
db = SQLAlchemy(app)