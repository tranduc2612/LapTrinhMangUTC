# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:27:37 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024
FORMAT = 'utf-8'

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sk.connect((host,port))
    
    print(sk.recv(1024).decode(FORMAT))
    
    Type = input("nhap loai: ")
    a = input("nhap so a: ")
    b = input("nhap so b: ")
    
    
    sk.send(Type.encode(FORMAT))
    sk.recv(1024)
    
    sk.send(a.encode(FORMAT))
    sk.recv(1024)
    
    sk.send(b.encode(FORMAT))
    sk.recv(1024)
    
    result = sk.recv(1024).decode(FORMAT)
    
    print(result)
    
    sk.close()