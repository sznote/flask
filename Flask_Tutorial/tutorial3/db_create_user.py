from app import db
from models import User

#insert  data
db.session.add(User("michael", "meichal@realpyhton.com", "i'll-never-tell") )
db.session.add(User("admin","ad@main","admin"))

db.session.commit()
