from flask import Blueprint, request, render_template
from main.models  import User 

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route("/")
def index():
	return "hello mod_authen"
