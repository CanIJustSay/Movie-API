from flask import Flask, jsonify, request
import csv
import pandas as pd 

app = Flask(__name__)

df = pd.read_csv('merged.csv')

data = [
    {
        "title":df["original_title"].tolist()
    },
    {
        "director":df["director"].tolist()
    },
    {
        "posterlink":df["posterlink"].tolist()
    },

]

@app.route('/getAD')

def getAd():
    return jsonify(({
        "data":data
    }))


if(__name__ == '__main__'):
    app.run(debug=True)