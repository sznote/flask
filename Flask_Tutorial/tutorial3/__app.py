#from flask import Flask, render_template, url_for, redirect,  url_for, request, session, flash, g
from flask import  render_template, url_for, redirect,  url_for, request, session, flash
from functools import wraps

# #import sqlite3
# app = Flask(__name__)
# # app.config['DEBUG'] = True
# # app.config['SECRET_KEY'] = "myname is sahai"
# # app.config['DATABASE'] = 'sample.db'
# # app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///tmp/posts.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #app.config.from_object('config.BaseConfig')

# #config
# import os
# app.config.from_object('config.DevelopmentConfig')
# #app.config.from_object(os.environ['APP_SETTINGS'])
# #export APP_SETTINGS='config.DevelopmentConfig'

# db = SQLAlchemy(app)
# bcrypt  = Bcrypt(app)

# from models import * 

# from project.users.views import users_blueprint

# app.register_blueprint(users_blueprint)

# # class Postsdb(db.Model):
# # 	id =  db.Column(db.Integer, primary_key=True)
# # 	title = db.Column(db.String(120))
# # 	description = db.Column(db.Text)

# # 	def __init__(self, title, description):
# # 		self.title = title
# # 		self.description = description

# # 	def  __repr__(self):
# # 		return '<tilte %r>' % self.title

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

		# # if  session['logined_in'] == True:
		# # 	flash("hello")	
		# try:
		# 	g.db  = connect_db()
		# 	cur = g.db.execute('select * from posts')
			
		# 	posts_dic={} #dict
		# 	posts = []  #list

		# 	for row in  cur.fetchall():
		# 		#posts_dic["title"] = row[0]
		# 		#posts_dic["description"] = row[1]
		# 		#posts.append(posts_dic)
		# 		posts.append(dict(title=row[0], description	=row[1]) )
		# 		#print  posts
		# 	#posts =  [dict(title=row[0], description=row[1]) for row in cur.fetchall() ]
		# 	g.db.close()
		#	except sqlit3.OperationError:
		#		flash("You have on  database!!")
		#posts = db.session.query(BlogPost).all()
		#posts  = BlogPost.query.all()
		posts = db.session.query(BlogPost).all()
		# BlogPost.query.all()
		#print posts.description

		return render_template("index.html", posts=posts)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	error = None
# 	if request.method ==  'POST':
# 		if request.form['username'] != 'admin' or  request.form['password'] != 'admin':
# 			error = 'Invalid credentials Plases try again.'
# 			print request.form['username']
# 		else:
# 			session['logined_in'] = True
# 			flash('You are login Success!!')
# 			return redirect(url_for('home'))
# 	return render_template("login.html",error=error)


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


@app.route('/logout')
@login_required
def logout():
	session.pop('logined_in',None)
	flash('You ware just logged out!!')
	#flash('fuck!!!!')
	return  redirect(url_for('welcome'))


# def connect_db():
# 	return sqlite3.connect(app.config['DATABASE'])

# if __name__ == "__main__":
# 	app.run()

# @app.route("/")
# def  index():
# 	#return "Hello World !!!"
# 	try: 
# 		mylogin = session['logined_in']
# 		if mylogin == True:
# 			mesg = "Login Sucess!!"
# 	except:
# 		mesg = "Not Login!"
	
# 	return render_template("index.html", mesg=mesg)
