# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:05:06 2023

@author: OSC
"""
import socket
host = 'localhost'
port = 2004


if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host,port))
    print(sk.recv(1024).decode('utf-8'))
    sk.send("Hello server".encode('utf-8'))
    while True:
        data = input('Enter message: ')
        sk.send(data.encode('utf-8'))
        data = sk.recv(1024)
        print(data.decode('utf-8'))
        
        
        
    