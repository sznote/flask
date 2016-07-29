from  tutorial1 import tutor1
from  flask import request, render_template
#from  . import tutorial1

@tutor1.route('/')
def index():
    if request.method.lower() == 'get':
        name = "sahai"
    return "Method userd: %s" % name

@tutor1.route("/bacon",methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably GET"
    
@tutor1.route('/profiles/<username>')
def profiles(username):
    return render_template("profiles.html",name=username)

@tutor1.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s <h2>" % post_id    
    
