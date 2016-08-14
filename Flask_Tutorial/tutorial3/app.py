from flask import Flask, render_template, url_for, redirect,  url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "myname is sahai"



def login_required(f):
	@wraps(f)
	def warp(*args, **kwargs):
		if 'logined_in' in session:
			return f(*args, **kwargs)
		else:
			flash ('@Loing_required You need to login  first.')
			return  redirect(url_for('login'))
	return warp

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

@app.route("/")
@login_required
def home():
		# if  session['logined_in'] == True:
		# 	flash("hello")	
		return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method ==  'POST':
		if request.form['username'] != 'admin' or  request.form['password'] != 'admin':
			error = 'Invalid credentials Plases try again.'
			print request.form['username']
		else:
			session['logined_in'] = True
			flash('You are login Success!!')
			return redirect(url_for('home'))
	return render_template("login.html",error=error)

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

if __name__ == "__main__":
	app.run()