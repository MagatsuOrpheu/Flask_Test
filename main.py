import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__) #the name of the application package
run_with_ngrok(app)

a = {
        "number": 1,
        "name": 'Mahesh',
        "age": 25,
        "city": "Bangalore",
        "country": "India"
}
b ={
        "number": 2,
        "name": 'Alex',
        "age": 26,
        "city": "London",
        "country": "UK"
}
c = {
        "number": 3,
        "name": 'David',
        "age": 27,
        "city": "San Francisco",
        "country": "USA"
}

d = {
        "number": 4,
        "name": 'John',
        "age": 28,
        "city": "Toronto",
        "country": "Canada"
}

e = {
        "number": 5,
        "name": 'Chris',
        "age": 29,
        "city": "Paris",
        "country": "France"
}

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"


@app.route("/input") #code to assign Input URL in our app to function input.

def input():
    list = (f"{a}"
            f"{b}"
            f"{c}"
            f"{d}"
            f"{e}")
    return jsonify(list) # "d" is the dictionary we defined


@app.route('/output', methods=['GET','POST']) #output page

def predJson():
    pred = r.choice(["positive","negative"])
    nd = d # our input
    nd["prediction"]=pred
    return jsonify(nd)

app.run()