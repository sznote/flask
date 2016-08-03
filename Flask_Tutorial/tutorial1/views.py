#from  tutorial1 import tutor1
from  flask import request, render_template
#from  . import tutorial1
from  . import tutor1
#import tutor1

@tutor1.route('/')
@tutor1.route('/<user>')
def index(user=None):
    if request.method.lower() == 'get':
        name = "sahai"
    #return "Method userd: %s" % name
    return render_template("user.html",user=user)

@tutor1.route("/shopping")
def shopping():
    food = [ "Cheese", "Tuna", "Beef" ] 
    return  render_template("shopping.html",food=food)
    
 #    
@tutor1.route("/bacon",methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably GET"
 #   
@tutor1.route('/profile/<username>')
def profiles(username):
    return render_template("profile.html",name=username)

 #   
@tutor1.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s <h2>" % post_id    
    
