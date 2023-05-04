import socket

# 新建socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接：
s.connect(('39.106.79.48', 9999))

# 接收消息：
print(s.recv(1024).decode('utf-8'))

# 发送数据：
data = b'20.0'
# data.replace(".", "")
s.send(data)

# 接收消息：
print(s.recv(1024).decode('utf-8'))

# 结束发送：
s.send(b'exit')
s.close()
