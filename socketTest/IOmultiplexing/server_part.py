import socket
import select
from queue import Queue

#创建socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置IP地址复用
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定对应的IP和端口号
server_address=("127.0.0.1",8888)
serversocket.bind(server_address)
#监听，并设置最大连接数
serversocket.listen(10)
serversocket.setblocking(False)
#超时时间
timeout=10
#创建epoll事件对象，后续要监控的事件全部添加到其中去
epoll=select.epoll()
#注册监听时间到等待读事件集合中
epoll.register(serversocket.fileno(),select.EPOLLIN)
#保存客户端连接消息的字典
message_queue={}
#文件句柄到对应对象的字典
fd_to_socket={serversocket.fileno():serversocket,}

while True:
    print("等待活动连接中...")
    events=epoll.poll(timeout)#被epoll_wait给阻塞，直到有事项或者超时后才会再次运行该程序
    if not events:
        print("epoll超时无活动连接，重新轮询...")
        continue
    print("有{}个新事件，开始处理".format(len(events)))

    for fd,event in events:
        socket=fd_to_socket[fd]#去文件句柄字典中查询
        if socket==serversocket:#如果是新的连接事件
            conn,address=serversocket.accept() #有事件后才使用accept系统调用去获得值
            print("有新的连接: "+str(address))
            #将新的连接设置为非阻塞连接并注册到事件集合中去
            conn.setblocking(False)
            epoll.register(conn.fileno(),select.EPOLLOUT)
            fd_to_socket[conn.fileno()]=conn
            #以新连接的对象为键值，值存储在队列中，保存每一个连接的信息
            message_queue[conn]=Queue()
            message="connection success!!"
            message_queue[conn].put(message.encode())
        elif event & select.EPOLLHUP: #事件关闭
            print("client close!")
            epoll.unregister(fd)
            fd_to_socket[fd].close()
            del fd_to_socket[fd]
        elif event & select.EPOLLIN: #可读事件
            data=socket.recv(1024)
            if data:
                print("收到数据来自客户端P{}的数据：{}".format(socket.getpeername(),data.decode()))
            message_queue[socket].put(data)
            epoll.modify(fd,select.EPOLLOUT)
        elif event & select.EPOLLOUT:
            try:
                msg=message_queue[socket].get_nowait()
            except:
                print(str(socket.getpeername())+" queue empty")
                epoll.modify(fd,select.EPOLLIN)
            else:
                print("发送数据: {}, 客户端： {}".format(msg.decode(),socket.getpeername()))
                socket.send(msg)
#在epoll中注销服务端文件句柄
epoll.unregister((serversocket.fileno()))
#关闭epoll
epoll.close()
serversocket.close()
