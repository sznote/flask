from flask import  Flask, render_template
from  content_managemant import Content
app = Flask(__name__)

@app.route('/')
def homepage():
	#return "Hi there, how ya doing?"
	return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
	#return "Hi there, how ya doing?"
	TOPIC_DICT = Content()
	return render_template('dashboard.html', TOPIC_DICT= TOPIC_DICT )

if __name__=='__main__':
	app.run(debug=True)