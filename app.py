from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    i=c=os.popen('curl -s http://169.254.169.254/latest/meta-data/instance-id/').read()
    return "v3 Instance %s says Hello, Flask!" % i

if __name__ == "__main__":
    app.run(port=80)
