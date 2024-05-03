from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Jubi\'s, Python World!'
