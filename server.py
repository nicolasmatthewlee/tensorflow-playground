import flask
from flask import Flask
import tensorflow as tf
import numpy as np

# load model
model = tf.keras.models.load_model('mnist-model')


def solve_predictions(predictions):
    'converts output of model.predict to the number with the highest activation'
    return list(map(lambda x: int(np.where(np.isclose(x, max(x)) == True)[0][0]), predictions))


# 1. create application instance
app = Flask(__name__)

# 2. assign handler functions to specific routes


@app.get('/')
def index():
    return '<h1>/</h1>'


@app.post('/api/model/predict')
def api_model_predict():
    data = flask.request.get_json()
    prediction = solve_predictions(model.predict([data]))
    return flask.jsonify(prediction[0])
