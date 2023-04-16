import flask
from flask import Flask

# 1. create application instance
app = Flask(__name__)

# 2. assign handler functions to specific routes


@app.get('/')
def index():
    return '<h1>/</h1>'


@app.post('/api/model/predict')
def api_model_predict():
    data = flask.request.get_json()
    print(data)
    return flask.jsonify(data)
