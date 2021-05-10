from socket import *

#创建服务端的socket
socketfd=socket(AF_INET,SOCK_STREAM)
#绑定IP与端口
socketfd.setblocking(False)
ip_port=('127.0.0.1',8888)
socketfd.bind(ip_port)
#设置最大连接数
socketfd.listen(5)

#设置连接表
conn_list=[]
print("开始接收连接...")
while True:
    #接收数据 连接对象和客户地址
    try:
        conn,address=socketfd.accept() #阻塞io，只有接收到了后才会继续运行
        print('接收来自{}的数据'.format(address))
        msg="连接成功"
        conn.send(msg.encode())
        conn.setblocking(False) #设置为非阻塞
        conn_list.append(conn) #将新的连接加入到后续遍历列表中
    except BlockingIOError:
        pass

    tmp_list=[conn for conn in conn_list]
    for conn in tmp_list:
        try:
            data=conn.recv(1024)
            print(str(address) + ': ' + data.decode())
            callback_data = 'data from server ' + data.decode()
            conn.send(callback_data.encode())
            #断开连接时的处理
            if data == b'exit':
                print('close conn',conn)
                conn.close()
                conn_list.remove(conn)
        except BlockingIOError:
            pass