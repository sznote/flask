from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask



app = Flask(__name__)

app.config['SECRET_KEY'] = "Hello saza"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bcrypt  = Bcrypt(app)
db =  SQLAlchemy(app)

import views


from models import User, Category, Post
# @app.route('/')
# def home():
#     return "Hello Word!!"

#if __name__ == '__main__':
#	app.run(debug=True)