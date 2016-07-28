from flask import  Flask
from tutorial1 import tutor1
from tutorial2 import tutorial2

app = Flask(__name__)
app.register_blueprint(tutor1, url_prefix='/tutor1')
app.register_blueprint(tutorial2, url_prefix='/tutor2')

app.run(debug=True)
