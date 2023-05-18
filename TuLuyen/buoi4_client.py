# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:10:37 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024;
FORMAT = 'utf-8'


if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sk.connect((host,port))
    
    message = sk.recv(1024).decode(FORMAT)
    
    print(message)
    
    while True:
        data = input("Send to Server: ")
        
        sk.send(data.encode(FORMAT))
        
        if(data == 'bye'):
            break;
        
        data = sk.recv(1024).decode(FORMAT)
        print(data)
        
        
        
    
    sk.close()