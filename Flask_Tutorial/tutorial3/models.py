from app import db

class BlogPost(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	descripton = db.Column(db.String, nullable=False)

	def __init__(self,title,descripton):
		self.title = title
		self.descripton =  descripton

	def __repr__(self):
		return '<{}>'.format(self.title, self.descripton)


	



