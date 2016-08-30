from flask import  Flask, render_template, flash, request, redirect, url_for
from  content_managemant import Content
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
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            #flash(attempted_username)
            #flash(attempted_password)
            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credential. Try Agian."
        return render_template("login.html",error=error)

    except Exception as e:
        #flash(e)
        return render_template("login.html",error=error)

        # if request.method == 'POST':
    #   print request.form['username']
    #return render_template('login.html',error=error)


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