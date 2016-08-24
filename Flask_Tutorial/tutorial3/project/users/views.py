from  flask import flash, redirect, render_template, request, \
	  url_for, Blueprint
#from functools  import wraps

from .forms  import LoginForm
from project.models import User, bcrypt
from flask_login import login_user, login_required, logout_user

#from project  import  bcrypt



users_blueprint = Blueprint( 
	'users', __name__,
	 template_folder='templates'
	)


# def login_required(test):
# 	@wraps(test)
# 	def wrap(*args, **kwargs):
# 		if 'logged_in' in session:
# 			return test(*args, **kwargs)
# 		else:
# 			flash ('You need to login frist!!')
# 			return redirect(url_for('users.login'))
# 	return wrap

###############
#### routes ###
###############



# @users_blueprint.route('/login',methods=['GET','POST'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		if (request.form['username'] != 'admin') or \
# 			 (request.form['password']  != 'admin'):
# 			error = 'Invalid credentials Plases try again.'
# 			print request.form['username']
# 		else:
# 			session['logged_in'] = True
# 			flash('You were logged in.')
# 			return redirect(url_for('home'))
# 	return render_template('login.html', error=error)



@users_blueprint.route('/login', methods=['GET', 'POST'])

def login():
	error = None
	form = LoginForm(request.form)

	if request.method ==  'POST':
		if form.validate_on_submit():
		 	user = User.query.filter_by(name=request.form['username']).first()
		 	if user is not None and bcrypt.check_password_hash(user.password,request.form['password'] ):
			# if request.form['username'] != 'admin' or  request.form['password'] != 'admin':
			# 	error = 'Invalid credentials Plases try again.'
			# 	print request.form['username']
			# else:
			#	session['logined_in'] = True
				login_user(user)
				flash('You are login Success!!')
				return redirect(url_for('home.home'))
			else:
				error = "Invalid credentials Plases try again."
		else:
			return render_template("login.html",form=form, error=error)
					
	return render_template("login.html",form=form, error=error)


@users_blueprint.route('/logout')
@login_required

def logout():
	#session.pop('logged_in', None)
	logout_user()
	#session.clear()
	flash('You were logged out')
	return redirect(url_for('home.welcome'))
