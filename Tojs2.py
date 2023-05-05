# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import *
import pymysql  # 导入操作数据库的库

app = Flask(__name__)

CORS(app, resources=r'/*')  # r'/*'是通配符，让本服务器所有的URL都允许跨越请求


@app.route('/hello')
def hello_world():
    # 连接数据库
    database = pymysql.connect(
        host="39.106.79.48",
        user="ysy",
        password="ysy514709635",
        database="My_Server"
    )
    cur = database.cursor()  # 取得游标

    sql = "SELECT * FROM data"
    cur.execute(sql)
    row_1 = cur.fetchone()
    return str(row_1[1])


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # 任何IP都可访问
        port=5000,  # 可用端口
        debug = True
    )
