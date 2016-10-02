from flask_sqlalchemy import SQLAlchemy
from app import app
from datatime import datetime


db = SQLAlchemy(app)

# class User(db.model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80), unique=True)
# 	email  = db.Column(db.String(120), unique=True)

# 	def  __init__(self, username, email):
# 		self.username = username
# 		self.email = email

# 	def __repr__(self):
# 		return "<user %r>" % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

# >>> py = Category('Python')
# >>> p = Post('Hello Python!', 'Python is pretty cool', py)
# >>> db.session.add(py)
# >>> db.session.add(p)
# Now because we declared posts as dynamic relationship in the backref it shows up as query:

# >>> py.posts
# <sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x1027d37d0>
# It behaves like a regular query object so we can ask it for all posts that are associated with our test “Python” category:

# >>> py.posts.all()
# [<Post 'Hello Python!'>]
