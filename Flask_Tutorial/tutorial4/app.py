import os
from flask  import Flask, render_template, request, redirect
from flask_sqlalchemy import  SQLAlchemy

app =  Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] =  'sqlite:///' + os.path.join(basedir, 'app.db')

#SQLALCHEMY_TRACK_MODIFICATIONS =  True

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



@app.route("/")
def index():
	return  render_template("add_user.html")

@app.route("/post_user", methods=['GET', 'POST'])
def post_user():
	if request.method == 'GET':
		return  "Please register  <br/>  <input type='button' value='register'>"
	else:
		user =  User(request.form['username'],request.form['email'])
		try:
			db.session.add(user)
			db.session.commit()
		except:
			return "Account and Email have Register"

		#return redirect(url_for('/'))
		return render_template("posts.html")


if __name__ == "__main__":
	app.run(debug=True)