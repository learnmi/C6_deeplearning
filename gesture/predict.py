import flask
from numpy import loadtxt
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

app = flask.Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    params = flask.request.json
    if (params==None):
        params = flask.request.args
    if (params!=None):
        data['response'] = params.get("msg")
        data["success"] = True
    return flask.jsonify(data)

app.run(host='0.0.0.0')

