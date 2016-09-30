from flask import Flask, render_template, url_for, redirect, request, flash

from form import registerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "Hello saza"

# @app.route('/')
# def  show_url_for():
# 	#return redirect( url_for('show_user_profile', username='sahai') )
# 	return url_for('show_user_profile', username='sahai') 

# @app.route('/profile/<username>')
# def show_user_profile(username):
# 	return "User: %s" % username

@app.route('/register',methods=['GET', 'POST'])
def register():
	form = registerForm(request.form)
	if form.validate_on_submit():
		return redirect('/success')
	return render_template('user/register.html', form=form)

@app.route('/success')
def success():
	return "Author registered!"

@app.route('/login', methods=['GET', 'POST'])
def login():

	error = None

	if request.method == 'POST':
		if valid_login(
				request.form['username'], 
				request.form['password']):
			return "Welcome Back,  %s" % request.form.get('username')
		else:
			error = "Incorrent username and password"
	return render_template("login.html", error=error)

def valid_login(username,password):
	#checks on the db if the nameme and password are correct.
	if username == password:
		return True
	else:
		return False


@app.route('/login2', methods=['GET', 'POST'])
def login2():
	if request.values:
	#if request.method == 'POST':
		bar = request.args.to_dict()
		for  x in bar:
				print "%s :: %s " % ( x, bar[x])

		#return  "User is %s" %  request.args.get('username')
		return render_template("login2.html", bar=bar)

		#return  "User is %s" %  request.values['username']
		#http://127.0.0.1:5000/login?username=saahai
	else:
		return '<form method="get" action="/login2"> \
			<p> \
			<input type="text" name="username" placeholder="username" required /> \
			</p> \
			<input type="password" name="password" placeholder="password" /> \
			<p> \
			<input type="submit" formnovalidate  value="submit" /> \
			<button type="submit"  > Summit </button> </p> </form>'

if __name__ == '__main__':
	app.run(debug=True)