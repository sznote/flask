from project import app, db
from project.models import  BlogPost
from flask import Flask, flash, redirect, session, url_for, render_template, Blueprint
from flask_login import login_required

from functools import wraps


home_blueprint = Blueprint(
    'homes', __name__,
    template_folder='templates'
)


##########################
#### helper functions ####
##########################

# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('users.login'))
#     return wrap


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string


    context =   { 'title': "Login Page",
                  'creator': "Sahai Srichock",
                }

    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts, context=context)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

