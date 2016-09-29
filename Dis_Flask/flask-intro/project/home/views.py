from project import app, db
from project.models import  BlogPost
from flask import Flask, flash, redirect, session, url_for, render_template, Blueprint, request
from flask_login import login_required, current_user

from functools import wraps
from forms import MessageForm


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
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # return "Hello, World!"  # return a string
    error = None
    print current_user.id

    context =   { 'title': "Login Page",
                  'creator': "Sahai Srichock",
                }
    #print "hello home"
    form =  MessageForm(request.form)

    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
            )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thank.')
        return redirect(url_for('homes.home'))
        #return render_template(
        #'index.html', posts=posts, error=error, form=form, context=context)
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, error=error, form=form, context=context)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

