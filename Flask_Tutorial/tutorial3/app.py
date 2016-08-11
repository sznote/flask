from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def  home():
	#return "Hello World !!!"
	return render_template("home.html")


if __name__ == "__main__":
	app.run()
