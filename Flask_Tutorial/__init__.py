from flask import  Flask
from .tutorial1 import tutor1
from .tutorial2 import tutorial2
from .tutorial3 import tutorial3
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.register_blueprint(tutor1, url_prefix='/tutor1')
app.register_blueprint(tutorial2, url_prefix='/tutor2')
app.register_blueprint(tutorial3, url_prefix='/tutor3')

app.config.from_pyfile('config_file.cfg')
#app.run(debug=True)
#db  = SQLAlchemy(app)
#app.run()