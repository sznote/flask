from  tutorial1 import tutor1
from  flask import request
#from  . import tutorial1

@tutor1.route('/')
def index():
    return "Method userd: %s" % request.method
 
@tutor1.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@tutor1.route('/profile/<username>')
def profile(username):
    return "<h2>Hey There %s <h2>" % username

@tutor1.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s <h2>" % post_id    
    
@tutor1.route('/about')  
def about():  
    return "about"