from flask import Flask, render_template, request
import TopSis as tp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadTopsis', methods=['POST', 'GET'])
def uploadTopsis():
    if request.method == 'POST':
        file = request.files['file']
        return calc_topsis(file)


def calc_topsis(file):
    df = tp.calcule(file)
    return df.to_html()