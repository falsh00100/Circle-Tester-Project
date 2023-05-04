import socket  # 导入scoket库
import threading  # 导入多线程库
import time  # 导入暂停时间库
import pymysql  # 导入操作数据库的库


# 创建socket（基于IPv4和TCP协议）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听端口
s.bind(('172.23.249.80', 9999))
s.listen(5)  # 监听，传入等待连接的最大数量，超过的连接需要等待
print('Waitting for connection...')  # 准备就绪


# 建立线程函数
def tcplink(sock, addr):
    print('Accpet new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')  # 向终端发送数据

    # 连接数据库
    database = pymysql.connect(host="39.106.79.48",
                               user="ysy",
                               password="ysy514709635",
                               # port="3306",
                               database="My_Server")
    cur = database.cursor()  # 取得游标

    while True:
        data = sock.recv(1024)  # 接收终端发送的数据
        time.sleep(1)  # 等待接收完成

        if not data or data.decode('utf-8') == 'exit':
            """"约定退出命令"""
            break

        sock.send(('Data received is %s' % data.decode('utf-8')).encode('utf-8'))

        # 转换数据并存入数据库中
        data_double = float(data.decode('utf-8'))
        sql = "insert into data values(5, %s)"  # SQL语句
        cur.execute(sql, data_double)
        database.commit()
        # 关闭连接
        cur.close()
        database.close()
        # sock.close()
        print('Connection from %s:%s close.' % addr)


# 开始监听
while True:
    # 接受一个新链接
    sock, addr = s.accept()
    # 创建一个新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
