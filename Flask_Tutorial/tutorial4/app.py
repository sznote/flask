import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

from flask_mail import Mail


app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECRET_KEY'] = 'super-secret'

app.config['MAIL_SERVER']='172.16.100.10'
app.config['MAIL_PORT'] = '25'
#SQLALCHEMY_TRACK_MODIFICATIONS =  True

mail = Mail()
mail.init_app(app)


db = SQLAlchemy(app)


# Define models

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r, %r>' % (self.username, self.email)
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='matt@nobien.net', password='password')
#     db.session.commit()



@app.route("/")
def index():
    myuser = User.query.all()
    #oneItem = User.query.filter_by(username="sahai").first()
    return render_template("add_user.html", myuser=myuser)

@app.route("/base")
def base():
    return render_template("home.html")

@app.route('/profile/<username>')
@login_required
def profile(username):
    myuser = User.query.filter_by(email=username).first()
    if myuser:
        return render_template("profile.html", myuser=myuser)
    else:
        return "User not found!!"


@app.route("/post_user", methods=['GET', 'POST'])
def post_user():
    if request.method == 'GET':
        return "Please register  <br/>  <input type='button' value='register'>"
    else:
        user = User(request.form['username'], request.form['email'])
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return "Account and Email have Register"

        return redirect(url_for('index'))
        # return render_template("posts.html")


if __name__ == "__main__":
    app.run(debug=True)