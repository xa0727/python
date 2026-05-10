import socket

socket_server=socket.socket()#创建socket对象
socket_server.bind(("localhost",8885))#绑定ip地址和窗口
socket_server.listen(1)#listen方法内接受一个整数传参数，表示接受的链接数量
conn,address=socket_server.accept()
#accept方法返回的是二元元组（链接对象，客户端地址信息）
#直接两个变量接收两个元素
#accept（）方法是阻塞方法，如果没有链接客户端，就卡在这一行
print(f"接收到了客户端的连接，客户端的信息是：{address}")
#接收客户端的信息,要使用客户端和服务端的本次链接对象

while True:
    data:str=conn.recv(1024).decode("utf-8")
    #recv接受的是参数是缓冲区大小一般1024
    #recv方法返回值是一个字节数组，不是字符串，用decode方法转换为字符串
    print(f"客户端发来的消息：{data}")
    msg=input("请输入你要和客户端回复的消息：")
    if msg=="exit":
        break
    conn.send(msg.encode("utf-8"))

conn.close()
socket_server.close()
