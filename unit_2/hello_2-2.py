from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent), 200


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)
