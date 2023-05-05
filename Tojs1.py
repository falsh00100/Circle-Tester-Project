# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import *

app = Flask(__name__)

CORS(app, resources=r'/*')  # r'/*'是通配符，让本服务器所有的URL都允许跨越请求


@app.route('/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # 任何端口都可访问
        port=5000,  # 可用端口
        debug = True
    )
