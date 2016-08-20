from project import db
from project.models import BlogPost

#create the database  adnthe db tables
db.create_all()
#insert 
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

db.session.commit()

# commit  the changes