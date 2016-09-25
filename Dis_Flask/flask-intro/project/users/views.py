
from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint

from form import LoginFrom
from functools import wraps
from project.models import User
from project import  bcrypt

################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

##########################
#### helper functions ####
##########################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginFrom(request.form)

    if request.method == 'POST':
        #print request.form['username']
        #print request.form['password']

        if form.validate_on_submit():

            user = User.query.filter_by(name=form.username.data).first()
            if user is not None  and bcrypt.check_password_hash(user.password, form.password.data): 
            #print "sss"
            # if (request.form['username'] != 'admin') \
            #         or request.form['password'] != 'admin':
            #     error = 'Invalid Credentials. Please try again.'
            # else:
                session['logged_in'] = True
                flash('You were logged in.')
                return redirect(url_for('homes.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('homes.welcome'))