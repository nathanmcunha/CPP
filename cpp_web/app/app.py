from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from numpy import linalg as la

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/uploadTopsis', methods = ['POST', 'GET'])
def uploadTopsis():
    if request.method == 'POST':
        file = request.files['file']
        # file_json = pd.json
        return calc_topsis(file)


def calc_topsis(file):
    file_df = pd.read_csv(file, index_col='nome')
    normalizado = normaliza(file_df)
    return normalizado.to_json()


def normaliza(data_frame):
    data_frame_normalizado = data_frame.apply(la.norm())

    return data_frame/data_frame_normalizado