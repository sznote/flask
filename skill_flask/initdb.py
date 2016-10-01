from app import db
from models import Blog
from models import User

# create tables 
db.drop_all
db.create_all()



# add data

user = User(
    "fullname", 
    "email@e.com",
    "username", 
    "password",
     True)
db.session.add(user)
db.session.flush()


print user.id
xid = db.session.query(User).filter_by(fullname='fullname').first()

print xid.id

if user.id:
    db.session.commit()
    db.session.add(Blog(name="sahai",admin=user.id))
    db.session.add(Blog(name="saza",admin=user.id))
    db.session.commit()
else:
    db.session.rollback()

# db.session.add(User("sahai",
#   "sahai@hotmail.com",
#   "saza",
#   "pass",
#   True)
# )

