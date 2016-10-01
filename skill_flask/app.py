from flask import Flask, render_template, url_for, redirect, request, flash, session, g
from form import registerForm, SetupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function




app = Flask(__name__)

app.config['SECRET_KEY'] = "Hello saza"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


from models import *


# @app.route('/')
# def  show_url_for():
#   #return redirect( url_for('show_user_profile', username='sahai') )
#   return url_for('show_user_profile', username='sahai') 

# @app.route('/profile/<username>')
# def show_user_profile(username):
#   return "User: %s" % username

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('login'))

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return  render_template("admin.html")

@app.route('/admin')
@login_required
def admin():
    #if 'username' in session:
    blogs = Blog.query.count()
    if blogs  == 0:
        return redirect(url_for('setup'))
    return render_template('admin.html')


@app.route('/setup',methods=['GET','POST'])
def setup():

    form =  SetupForm(request.form)   
    error = None     
    if form.validate_on_submit():
        user =  User(
            form.fullname.data , 
            form.email.data, 
            form.username.data, 
            form.password.data,
            True
        )

        db.session.add(user)
        db.session.flush()
        #db.session.commit()
        if user.id:
           
            blog = Blog(form.username.data,user.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        
        if user.id and blog.id:
            db.session.commit()
            flash("Blog Created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error create blog"

    return render_template("setup.html",  form=form)


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

    form = LoginForm(request.form)

    if request.method == 'POST':
        # if valid_login(
        #         request.form['username'], 
        #         request.form['password']):
        #     return "Welcome Back,  %s" % request.form.get('username')
        # else:
        #     error = "Incorrent username and password"
        if  form.validate_on_submit():
            user = User.query.filter_by(
             username=form.username.data,
             password=form.password.data).limit(1)

            if user.count():
                #session['username'] = form.username.data
                session['logged_in'] = True
                
                return redirect('/login_success')
            else:
                error = "Incorrect !!"
    return render_template("user/login.html", error=error, form=form)

@app.route('/login_success')
def login_success():
    return  'Author login !!'


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

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    return "POST"
    
if __name__ == '__main__':
    app.run(debug=True)