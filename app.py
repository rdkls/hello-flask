#!/usr/bin/env python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    i = 'local'
    instanceid = os.popen('curl --max-time 1 -s http://169.254.169.254/latest/meta-data/instance-id/').read()
    if instanceid:
        i = instanceid
    return "Hello from instance %s!" % i

if __name__ == "__main__":
    app.run(port=8888)
