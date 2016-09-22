#from flask_sqlalchemy import SQLAlchemy
from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):

	__tablename__ = "posts"
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description  = db.Column(db.String(100), nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self,title, description):
		self.title = title
		self.description = description

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
		self.password = password

	def __repr__(self):
		return '<name {}'.format(self.name)

#  BlogPost.author_id[users.id]