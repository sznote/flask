from project import app, db
from project import BlogPost
from flask import  render_template, url_for, redirect,  url_for, request, session, flash
from functools import wraps


def login_required(f):
	@wraps(f)
	def warp(*args, **kwargs):
		if 'logined_in' in session:
			return f(*args, **kwargs)
		else:
			flash ('@Loing_required You need to login  first.')
			return  redirect(url_for('users.login'))
	return warp



@app.route("/")
@login_required
def home():
		posts = db.session.query(BlogPost).all()
		return render_template("index.html", posts=posts)


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


@app.route('/logout')
@login_required
def logout():
	session.pop('logined_in',None)
	flash('You ware just logged out!!')
	return  redirect(url_for('welcome'))
