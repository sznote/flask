from flask import  Flask, render_template, flash, request, redirect, url_for, session
from content_managemant import Content
from dbconnect import connection

from flask_wtf import Form
from wtforms  import  BooleanField, TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from passlib.hash import sha256_crypt
from MySQLdb import  escape_string as thwart
import gc



app = Flask(__name__)


app.secret_key = 'some_secret'

@app.route('/')
def homepage():
    #return "Hi there, how ya doing?"
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    #return "Hi there, how ya doing?"
    TOPIC_DICT = Content()
    flash ("flash test !!!")
    flash ("flash test1 !!!")
    flash ("flash test2 !!!")

    return render_template('dashboard.html', TOPIC_DICT= TOPIC_DICT )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.errorhandler(404)
# def page_not_found(e):
#   return render_template('404.html'), 404


@app.route('/login/', methods = ['GET','POST'])
def login_page():
    error = ''
    
    try:       
        if request.method == "POST":
            c, conn =  connection()
            
            #print ("asdfasdf %s, %s") %("100","200")
            #a = "100 + 200 + %s"  %  "100"  * note  not , 

            #a = "100","200","300"
            #('100', '200', '300')


            data =  c.execute("SELECT *  FROM users WHERE username  = %s",  [ thwart (  request.form['username'] ) ] )
            #sql = "SELECT *  FROM users WHERE username  = %s"  %( thwart (request.form['username'] ))
            #print sql 
            #data =  c.execute( "SELECT *  FROM users WHERE username  = '%s'"  %( thwart (request.form['username'] )) )
            
            data  = c.fetchone()[2]
            
            

            if sha256_crypt.verify(request.form['password'], data ):
                session ['logged_in']  = True
                session ['username'] = request.form['username']
                session ['admin'] = True
                flash ("Yous are now logged in")
                return redirect( url_for("dashboard") )
            else:
                error = "Invalid credentials, Try again."

        gc.collect()

        return render_template("login.html", error = error)
    


#            attempted_username = request.form['username']
#            attempted_password = request.form['password']

    except Exception as e:
        #flash(e)
        error = "Invalid credentials, try again"
        return render_template("login.html",error=error)


class RegistrationForm(Form):

    username = TextField('username', validators=[DataRequired(), Length(min=4,max=20)] )
    email =    TextField("Email Address", validators=[Length(min=6,max=50)])  
    password = PasswordField('Password', validators=[DataRequired(), 
                                        EqualTo('confirm', message='Passwords must match')] )

    confirm =  PasswordField('Repeate Password')
    accept_tos = BooleanField('I accept the Team of Service',validators=[DataRequired()])


    # username = TextField('Username', [validators.DataRequired(), validators.Length(min=4, max=20)])
    # email =    TextField('Email Address', [validators.DataRequired(), validators.Length(min=4, max=50)] )
    # password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])

    # confirm = PasswordField('Repeate Password')
    # accept_tos = BooleanField('I accept the Team of Service',[validators.DataRequired()])



@app.route('/register/', methods = ['GET','POST'])
def register_page():
    try:
        #c, conn = connection()
        form = RegistrationForm(request.form)

        

        #if request.method == 'POST' and form.validate_on_submit():
        if request.method == 'POST' and form.validate():

            print "POST !!!!!!"   
        
            username =  form.username.data
            #username =  request.form['username']
            email = form.email.data

            password =  sha256_crypt.encrypt((str(form.password.data)))
            

            c, conn = connection()

            x = c.execute("SELECT * from  users where username = %s", [ thwart(username) ] )

            #x =  c.execute("SELECT * from users where username = %s", [username] )

            if  int(x) > 0 :
                #print "found user!!"
                flash(" That username is already taken, please choose another")
                return render_template('register.html', form=form)
            else:
                c.execute("insert into users (username, password, email, tracking) values (%s, %s, %s,%s)",
                    (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/") ))
                conn.commit()
                flash("Thanks for Register!")
            conn.close()
            gc.collect()
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))

        return render_template("register.html",form=form)
        
    except Exception as e:
        return(str(e))



@app.route('/slashboard/')
def slashboard():
    #return "Hi there, how ya doing?"
    TOPIC_DICT = Content()
    try:
        return render_template('dashboard.html', TOPIC_DICT= WOOP_DICT )
    except Exception as e:
        return render_template('505.html', error=e )

if __name__=='__main__':
    app.run(debug=True)