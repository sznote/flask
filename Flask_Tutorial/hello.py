from  flask import  Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/list")
def list():
    return "List products"
    
if __name__ == "__main__":
    app.run()
    