from tutorial2 import tutorial2
from flask import render_template
from flask_sqlalchemy import  SQLAlchemy
#from models import db
from   models   import db



@tutorial2.route('/')
def index():
    return render_template("tutorial2.html")