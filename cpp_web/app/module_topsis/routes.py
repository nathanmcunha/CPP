import os
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request, redirect, session,flash , url_for
import pandas
import numpy
from numpy import linalg as ls

app = Flask(__name__)
app.secret_key = 'cpp'


@app.route('/cpp', method=['GET', 'POST'])
def cpp():
    if 'file' not in request.file:
        flash('Sem Arquivo')
        return jsonify('Falhou')
    file = request.file['file']


    return True