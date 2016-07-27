from  flask import  Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/list")
def list():
    return "List products"
    
@app.route('/detail/<name>')
def detail(name):
    return "Hello" + name + "!!"
    
if __name__ == "__main__":
    app.run()
    