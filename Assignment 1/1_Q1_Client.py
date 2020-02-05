#import socket
#s = socket.socket()
#host = '127.0.0.1'
#port = 3000
#s.connect((host,port))
#print("Connected to Server")

#while(1):
#    message = input()
#    s.send(message.encode())
#    mess = s.recv(1024)
#    print("Server : ", mess.decode())
#s.close()




import socket

def client_program():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 3000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message = input(" -> ")  # take input
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
    client_socket.close()  # close the connection
client_program()
