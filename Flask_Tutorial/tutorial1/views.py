from  tutorial1 import tutor1
#from  . import tutorial1

@tutor1.route('/')
def index():
    return "hello tutorial1"
   
@tutor1.route('/fuck')  
def fuck():  
    return "fuck"