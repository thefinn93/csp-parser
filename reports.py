#!/usr/bin/env python
import json
import dataset
from flask import Flask, request, jsonify, render_template
from urlparse import urlparse

app = Flask(__name__)
app.config.from_pyfile('default-config.py')
app.config.from_pyfile('config.py', silent=True)

db = dataset.connect(app.config['DATABASE'])


@app.route("/")
def index():
    return render_template('index.html', domains=db['reports'].distinct('domain'))


@app.route("/<domain>")
def domain_report(domain):
    return render_template('report.html', reports=db['reports'].find(domain=domain))


@app.route("/csp", methods=["POST"])
def csp():
    data = json.loads(request.data)['csp-report']
    row = dict()
    for key in data:
        row[key.replace("-", "_")] = data[key]
    if "document-uri" in data:
        url = urlparse(data['document-uri'])
        if url.scheme != "view-source":
            row['domain'] = url.netloc
        else:
            url = urlparse(url.path)
            row['domain'] = url.netloc
    db['reports'].insert(row)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run()
