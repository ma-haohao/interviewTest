import socket

client=socket.socket()#建立socket
ip_port=('127.0.0.1',8888)
#连接主机
client.connect(ip_port)
#定义发送循环信息
while True:
    #接收主机信息，每次接收缓冲区1024个字节
    data=client.recv(1024) #阻塞IO=，仅当接收到数据后该进程才继续运行
    print(data.decode())
    msg_input=input("请输入发送的信息: ")
    client.send(msg_input.encode())
    if msg_input=='exit':
        break
