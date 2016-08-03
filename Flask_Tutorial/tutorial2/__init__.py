from flask import Blueprint, current_app
tutorial2 =  Blueprint('tutorial2', __name__, template_folder='templates', static_folder='static')

print tutorial2.root_path
from tutorial2  import views