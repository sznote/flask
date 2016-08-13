from flask import Flask, render_template, url_for, redirect,  url_for, request

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def  home():
	#return "Hello World !!!"
	return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method ==  'POST':
		if request.form['username'] != 'admin' or  request.form['password'] != 'admin':
			error = 'Invalid credentials Plases try again.'
			print request.form['username']
		else:
			return redirect(url_for('home'))
	return render_template("login.html",error=error)


if __name__ == "__main__":
	app.run()