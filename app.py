# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:59:37 2020

@author: jansen
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open("model.pkl", "rb"))

model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/predict", methods=["GET"])
def predict():

    experience = float(request.args.get("experience"))
    test_score = float(request.args.get("test_score"))
    rev_score = float(request.args.get("rev_score"))

    
    predicted_salary = model.predict([[experience, test_score, rev_score]])
    return jsonify({"predicted_salary": round(predicted_salary[0],2)})

    
if __name__ == "__main__":
    app.run(debug = True)
