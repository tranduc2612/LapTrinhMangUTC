# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:06:41 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024;
FORMAT = 'utf-8'


if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sk.bind((host,port))
    
    sk.listen()
    
    print("listen client...")
    
    conn,address = sk.accept()
    
    data = 'hello client !'.encode(FORMAT)
    conn.sendall(data)
    
    while True:
        data = conn.recv(1024).decode(FORMAT)
        if(data == 'bye'):
            break;
        print(data)
        data = input("Text something: ").encode(FORMAT)
        conn.sendall(data)
    
    sk.close()