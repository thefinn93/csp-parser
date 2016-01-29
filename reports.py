#!/usr/bin/env python
from flask import Flask, request, jsonify
app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/csp", methods=["POST"])
def csp():
    data = request.get_json()
    app.logger.warning('Got some JSON! %s', data)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run()
