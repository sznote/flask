from flask import  Flask, render_template, request, url_for, redirect, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#import sqlite3
#import gc


app = Flask(__name__)
bcrypt = Bcrypt(app)

# config 

import os
app.config.from_object(os.environ['APP_SETTINGS'])


#app.config.from_object('config.BaseConfig')

#create the sqlalchemy object
db = SQLAlchemy(app)

from models import *


def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return  redirect(url_for('login'))
	return wrap


@app.route('/')
@login_required
def home():
	#return "hello world!!"
	posts = db.session.query(BlogPost).all()

	print posts

	context =   { 'title': "Login Page",
				  'creator': "Sahai Srichock",
				}

	return  render_template("index.html", posts=posts, context=context)



@app.route('/welcome')
def fwelcome():
	#return "Welcome !!"
	return render_template("welcome.html")

@app.route('/show')
def show():
	name = request.args.get('name')
	if name is not None:	
		return name
	else:
		return "Hi! Guest" 


@app.route('/login', methods=['GET', 'POST'])
def login():

	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. please try again.'
		else:
			session['logged_in'] = True
			flash ('You were just logged in!')
			return redirect(url_for('home'))
	return  render_template("login.html", error=error)


@app.route('/logout')
@login_required
def logout():
	if  "logged_in" in session:
		print session['logged_in']
	flash('You were just logged out !!')	
	session.pop('logged_in', None)
	#print url_for('fwelcome') // retrun  /wecome
	return redirect(url_for('fwelcome'))


# def connect_db():
# 	return sqlite3.connect(app.database)


if __name__ ==  '__main__':
	app.run(debug=True)
