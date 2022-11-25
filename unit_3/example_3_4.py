from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__, template_folder='../templates')
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user_bootstrap.html', name=name)
