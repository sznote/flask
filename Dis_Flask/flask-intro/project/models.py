#from flask_sqlalchemy import SQLAlchemy
from project import db
from project import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):

	__tablename__ = "posts"
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description  = db.Column(db.String(100), nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self,title, description, author_id):
		self.title = title
		self.description = description
		self.author_id = author_id

	def  __repr__(self):
		return  '<tilte {}'. format(self.title)

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	email = db.Column(db.String(60), nullable=False)
	password = db.Column(db.String(60), nullable=False)
	posts = relationship("BlogPost", backref="author")


	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password)

	def __repr__(self):
		return '<name {}'.format(self.name)

	def is_active(self):
		return True

	def is_authenticated(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return  unicode(self.id)



#  BlogPost.author_id[users.id]
#  xxxx.author.name  , #Reference  author. 