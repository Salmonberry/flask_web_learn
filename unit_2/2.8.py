from flask import make_response, Flask, redirect, abort

app = Flask(__name__)


# 响应对象 make_response
@app.route('/')
def index():
    # return '<h1>Bad Request</h1>', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# 重定向辅助对象 redirect（）
@app.route('/')
def index():
    return redirect('https://www.baidu.com/')

# abort抛出异常
# @app.route('/user/<id>')
# def get_user(id):
# user = load_user(id)
# if not user:
#     abort(404)
# return '<h1>Hello,{}</h1>'.format(user.name)
