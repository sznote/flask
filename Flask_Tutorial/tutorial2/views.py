#from tutorial2 import tutorial2
from flask import render_template
from  init  import tutorial2

  
#from flask_sqlalchemy import  SQLAlchemy

#from app  import db
#from tutorial3 import tutorial3
#from main.models import mydb
#from main.models import User

@tutorial2.route('/')
def index():
    return render_template("tutorial2.html")
