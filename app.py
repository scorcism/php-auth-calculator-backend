from flask import Flask
app = Flask(__name__)

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<h1>Hello World!!!</h1>"


@app.route("/add/<query>")
@cross_origin()
def add(query):
    q = query.split(",")
    ans = int(q[0]) + int(q[1])
    return f"{ans}"

@app.route("/sub/<query>")
def sub(query):
    q = query.split(",")
    ans = int(q[0]) - int(q[1])
    return f"{ans}"

@app.route("/mul/<query>")
def mul(query):
    q = query.split(",")
    ans = int(q[0]) * int(q[1])
    return f"{ans}"

@app.route("/div/<query>")
def div(query):
    q = query.split(",")
    ans = int(q[0]) / int(q[1])
    return f"{ans}"

@app.route("/mod/<query>")
def mod(query):
    q = query.split(",")
    ans = int(q[0]) % int(q[1])
    return f"{ans}"

if __name__=="__main__":
    app.run(debug=True);

