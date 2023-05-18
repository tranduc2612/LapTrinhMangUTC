import socket
import sys

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print('Socket created')
    host = 'localhost'
    port = 9050
    
    sk.bind((host, port))
    print('Socket bind to %s port %s'%(host, port))
    sk.listen(5)
    print('waiting')
    client_sk, client_addr = sk.accept()
    print('Client address ', client_addr)
    data = 'Hello client'
    client_sk.send(data.encode('utf-8'))
    
    while True:
        data = client_sk.recv(1024)
        if data.decode('utf-8') == 'bye':
            print(data.decode('utf-8'))
            client_sk.close()
            
            print('waiting')
            client_sk, client_addr = sk.accept()
            print('Client address ', client_addr)
            data = 'Hello client'
            client_sk.send(data.encode('utf-8'))
            continue
            
        print(data.decode('utf-8'))
        data = input("Enter message: ")
        client_sk.send(data.encode('utf-8'))