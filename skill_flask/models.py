# from app import  bcrypt
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy

from init import db, bcrypt, uploaded_images
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import  relationship
from datetime import datetime


class Blog(db.Model):

    __tablename__ = 'blog'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer,  db.ForeignKey('users.id'))

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return '<Name %r' % self.name

class  User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35),  unique=True)
    username = db.Column(db.String(35),unique=True)
    password = db.Column(db.String(80))
    is_author = db.Column(db.Boolean)

    posts =  db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, fullname, email, username, password, is_author=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = self.password = bcrypt.generate_password_hash(password)
        self.is_author = is_author

    def __repr__(self):
        return '<User %r' % self.username

class Post(db.Model):
    __tablename__= 'post'
    id = db.Column(db.Integer, primary_key=True)
    blog_id  =  db.Column(db.Integer, db.ForeignKey('blog.id'))
    user_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(30))
    body = db.Column(db.Text)
    image = db.Column(db.String(255))
    slug = db.Column(db.String(256), unique=True)
    publish_date = db.Column(db.DateTime())
    live = db.Column(db.Boolean)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', 
        backref=db.backref('posts', lazy='dynamic') )

    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)

    def __init__  (self, blog, author, title, body, category, slug, image=None,  publish_date=None, live=True):

        self.blog_id = blog.id
        self.user_id = author.id
        self.title =  title
        self.body = body
        self.category =  category
        self.publish_date = publish_date
        self.live = live
        self.slug = slug
        self.image = image
        if publish_date is None:
            self.publish_date = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>'  % self.title

class Category(db.Model):

    __tablename__ =  'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        #return '<Category %r>' % self.name
        return self.name
