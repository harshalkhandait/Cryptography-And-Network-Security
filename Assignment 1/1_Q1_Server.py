#import socket
#s = socket.socket()
#host = '127.0.0.1'
#print(host)
#port = 3000
#s.bind((host,port))
#s.listen(2)
#print("Waiting for connection")
#temp = s.accept()
#con1soc = temp[0]
#con1add = temp[1]
#print("Successful! Connection is stablished with :-")
#print("socket :- ", con1soc)
#print("")
#print("socket :- ", con1add)
#while(1):
#    mess = input()
#    con1soc.send(mess.encode())
#    print("Succesfully! Message sent")
    #print(temp1.recv(1024).decode())
#temp.close()


import socket


def server_program():
    # get the hostname
    host = '127.0.0.1'
    port = 3000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


server_program()
