from project import db, bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class BlogPost(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self,title,description):
		self.title = title
		self.description =  description


	def __repr__(self):
	# 	return '(title: {}, descripton:{})'.format(self.title, self.descripton)
		return '<title {}> '. format(self.title)
			

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	posts =  relationship("BlogPost", backref="author")

	def __init__(self,name,email,password):
		self.email = email
		self.name = name		
		self.password = bcrypt.generate_password_hash(password)


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def  get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<name {}>'. format(self.name)
