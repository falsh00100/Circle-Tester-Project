import socket  # 导入scoket库
import threading  # 导入多线程库
import time  # 导入暂停时间库

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
    while True:
        data = sock.recv(1024)  # 接收终端发送的数据
        time.sleep(1)  # 等待接收完成

        if not data or data.decode('utf-8') == 'exit':
            """"约定退出命令"""
            break

        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
        # sock.close()
        print('Connection from %s:%s close.' % addr)


# 开始监听
while True:
    # 接受一个新链接
    sock, addr = s.accept()
    # 创建一个新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
