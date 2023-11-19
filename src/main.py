from flask import Flask

app = Flask(__name__)

@app.route("/health_check")
def hello_world():
    return "Success"