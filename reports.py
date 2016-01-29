#!/usr/bin/env python
import json
import dataset
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_pyfile('default-config.py')
app.config.from_pyfile('config.py', silent=True)

db = dataset.connect(app.config['DATABASE'])
reports = db['reports']


@app.route("/")
def hello():
    return jsonify(reports.find())


@app.route("/csp", methods=["POST"])
def csp():
    row = dict(json.loads(request.data)['csp-report'])
    reports.insert(row)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run()
