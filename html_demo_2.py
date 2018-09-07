from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/datahostingdemo")
def data():
    v = "a variable with some data"
    l = ['a','b','c','d','e']
    d = {'first': 'Jane','last':'Smith'}
    return render_template("data.html",v = v,l = l, d = d)

app.run(debug = True, host = "0.0.0.0", port =5000)