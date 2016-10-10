from __init__ import db
from datetime import datetime


class PostPic(db.Model):
    __tablename__ = "postpic"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    publish_date = db.Column(db.DateTime())

    def __init__(self, image, publish_date=None):
        self.image = image
        if publish_date is None:
            self.publish_date = datetime.utcnow()

    def __repr__(self):
        return "<image %r" % self.image


# class  User(db.Model):
#     __tablename__ = "user"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return "<test %r" % self.test