from app  import db
from models  import User


#insert data

db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("admin","admin@min.com","admin"))

db.session.commit()
