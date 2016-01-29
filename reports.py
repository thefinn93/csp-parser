#!/usr/bin/env python
import json
import dataset
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config.from_pyfile('default-config.py')
app.config.from_pyfile('config.py', silent=True)

db = dataset.connect(app.config['DATABASE'])


@app.route("/")
def hello():
    return render_template('index.html', reports=db['reports'].all())


@app.route("/csp", methods=["POST"])
def csp():
    try:
        data = json.loads(request.data)['csp-report']
        row = dict()
        for key in data:
            row[key.replace("-", "_")] = data[key]
        db['reports'].insert(row)
        return jsonify({"success": True})
    except KeyboardInterrupt:
        return(jsonify({"success": False, "data": request.data}))


if __name__ == "__main__":
    app.run()
