#!/usr/bin/env python
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

handler = RotatingFileHandler('csp.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/csp", methods=["POST"])
def csp():
    data = request.get_json()
    app.logger.info(json.dumps(data))
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run()
