# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:35:09 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024
FORMAT = 'utf-8'


if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   
    sk.connect((host,port))

    message = sk.recv(1024).decode(FORMAT)
    print(message)
    
    data = input("Nhap du lieu :")
    sk.sendall(data.encode(FORMAT))
    
    data = sk.recv(1024).decode(FORMAT)
    
    print(data)
    
    sk.close()