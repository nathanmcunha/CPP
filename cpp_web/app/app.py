from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from numpy import linalg as la
import csv as csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/uploadTopsis', methods=['POST', 'GET'])
def uploadTopsis():
    if request.method == 'POST':
        file = request.files['file']
        pesos = request.form['file_pesos']
        return calc_topsis(file, pesos)


def calc_topsis(file, pesos = []):

    file_df = pd.read_csv(file, index_col='nome')
    normalizado = normaliza(file_df)
    # pesos = [-0.25, 0.5, 0.15, 0.1]
    ponderado = ponderar(normalizado, pesos)
    nis = ponderado.min()
    pis = ponderado.max()
    difer_max = diferenca(ponderado, pis)
    difer_min = diferenca(ponderado, nis)
    coef = coeficientes(difer_max, difer_min)
    coef_df = pd.DataFrame(coef, columns=['coeficiente'])
    coef_df.sort_values(by=['coeficiente'], ascending=False)

    return coef_df.to_json()


def normaliza(data_frame):
    data_frame_normalizado = data_frame.apply(la.norm)
    return data_frame/data_frame_normalizado


def ponderar(normalizado, pesos):
    return normalizado * pesos


def diferenca(ponderado, x):
    aux = (ponderado - x)**2
    aux = aux.sum(axis=1)
    aux = np.sqrt(aux)
    return aux


def coeficientes(difer_max, difer_min):
    return difer_min/(difer_max + difer_min)

