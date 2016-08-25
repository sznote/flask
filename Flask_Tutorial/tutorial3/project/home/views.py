from project import app, db
from project.models import BlogPost
from flask import  render_template, url_for, redirect,  url_for, request,  flash, Blueprint
from functools import wraps
from flask_login import login_required, current_user
from .forms import MessageForm

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# def login_required(test):
# 	@wraps(test)
# 	def warp(*args, **kwargs):
# 		if 'logged_in' in session:
# 			return test(*args, **kwargs)
# 		else:
# 			flash ('@Loing_required You need to login  first.')
# 			return  redirect(url_for('users.login'))
# 	return warp



# @home_blueprint.route("/")
# @login_required
# def home():
# 		posts = db.session.query(BlogPost).all()
# 		return render_template("index.html", posts=posts)



@home_blueprint.route('/', methods=['GET','POST'])
@login_required
def home():
	error = None
	form = MessageForm(request.form)

	if form.validate_on_submit():
		new_message = BlogPost(
			form.title.data,
			form.description.data,
			current_user.id
			)
		db.session.add(new_message)
		db.session.commit()
		flash('New entry was successfully posted. Thank.')
		return redirect(url_for('home.home'))
	else:
		posts  = db.session.query(BlogPost).all()
		return render_template("index.html", posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
#@login_required
def welcome():
	return render_template('welcome.html')


# @app.route('/logout')
# @login_required
# def logout():
# 	session.pop('logined_in',None)
# 	flash('You ware just logged out!!')
# 	return  redirect(url_for('welcome'))
