from flask import Flask, render_template, url_for, redirect,  url_for, request, session, flash


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "myname is sahai"



@app.route("/")
def  index():
	#return "Hello World !!!"
	try: 
		mylogin = session['logined_in']
		if mylogin == True:
			mesg = "Login Sucess!!"
	except:
		mesg = "Not Login!"
	
	return render_template("home.html", mesg=mesg)

@app.route("/home")
def home():
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
			flash('You ware just logged in!!')
			return redirect(url_for('home'))
	return render_template("login.html",error=error)

@app.route('/logout')
def logout():
	session.pop('logined_in',None)
	flash('You ware just logged in!!')
	return  redirect(url_for('home'))

if __name__ == "__main__":
	app.run()