from  flask import  Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    x = 100 + 100
    return "Good bye World!"

@app.route("/list")
def list():
    return "List products"
    
@app.route('/user/<username>')
def user(username):
    return  render_template('profile.html',
                             name=username)
@app.route("/lotsofdata")
def people():
    my_people = {'Alice': 25,
                 'Bob': 21,
                 'Charlie': 20,
                 'Doug': 28}
                 
    return jsonify(my_people)
                

                             
if __name__ == "__main__":
    app.run(debug=True)
    