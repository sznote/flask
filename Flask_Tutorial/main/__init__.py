from flask import  Flask
from tutorial1 import tutor1
from tutorial2.init import tutorial2
from tutorial3 import tutorial3
from main.auta.views import mod_auth as auth_module 

#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.register_blueprint(tutor1, url_prefix='/tutor1')
app.register_blueprint(tutorial2, url_prefix='/tutor2')
app.register_blueprint(tutorial3, url_prefix='/tutor3')

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
# This will create the database file using SQLAlchemy
db.create_all()
