# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:25:51 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 9050

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("Tạo soc ket thanh cong")
    sk.bind((host,port))
    sk.listen()
    print("Server")
    print("Waiting client...")
    
    client_sk, client_addr = sk.accept()
    data = 'hello client'
    client_sk.send(data.encode('utf-8'))
    print(client_sk.recv(1024).decode('utf-8'))
    
    while True:
        data = client_sk.recv(1024)
        if data == "bye":
            break;
        print(data.decode('utf-8'))
        mess = input("Enter message: ")
        client_sk.send(mess.encode('utf-8'))
    
    
    