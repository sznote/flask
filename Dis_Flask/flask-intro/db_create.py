from app import db
from models import BlogPost

#create  the databbase ant th e db tables
db.create_all()

#insert
db.session.add(BlogPost("Goold", "I\'m good"))
db.session.add(BlogPost("Well ", "I\'m well!")) 


#commit the changes
db.session.commit()