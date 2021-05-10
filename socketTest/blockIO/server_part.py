from socket import *
from threading import Thread

#为每一个连接单独建立一个线程
def communicate(conn,address):
    while True:
        #接收客户端数据消息
        data=conn.recv(1024)
        print(str(address)+': '+data.decode())
        if data==b'exit':
            break
        callback_data='data from server '+data.decode()
        conn.send(callback_data.encode())
    conn.close()

#创建服务端的socket
socketfd=socket(AF_INET,SOCK_STREAM)
#绑定IP与端口
ip_port=('127.0.0.1',8888)
socketfd.bind(ip_port)
#设置最大连接数
socketfd.listen(2)

while True:
    print('正在等待接收数据…')
    #接收数据 连接对象和客户地址
    conn,address=socketfd.accept() #阻塞io，只有接收到了后才会继续运行
    print('接收来自{}的数据'.format(address))
    msg="连接成功"
    conn.send(msg.encode())
    t=Thread(target=communicate,args=(conn,address))
    t.start()