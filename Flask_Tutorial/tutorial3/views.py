#from tutorial3 import tutorial3
from . import  tutorial3

@tutorial3.route('/')

def index():
    return "hello tutorial3"