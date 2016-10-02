from flask import Flask 

app.config[]
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
@app.route('/')
def index():
	return "Hello World"

if __name__=='__main__':
	app.run(debug=True)