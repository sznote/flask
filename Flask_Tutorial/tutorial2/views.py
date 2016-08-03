#from tutorial2 import tutorial2
from flask import render_template
from . import tutorial2

  
#from flask_sqlalchemy import  SQLAlchemy

#from app  import db
#from tutorial3 import tutorial3
#from models import db


@tutorial2.route('/')

def index():
    return render_template("tutorial2.html")