# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:20:54 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024
FORMAT = 'utf-8'


def solve(a,b,Type):
        if Type == 'Min':
            if(a<=b):
                return a
            else:
                return b
        elif Type == 'Max':
            if(a>=b):
                return a
            else:
                return b
        else:
            print('defaul')
    

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sk.bind((host,port))
    sk.listen()
    
    print('listen client...')
    
    conn,address = sk.accept()
    print("connect to ", address)
    
    conn.send('hello client'.encode(FORMAT))
    
    Type = conn.recv(1024).decode(FORMAT)
    conn.send(Type.encode(FORMAT))
    
    a = conn.recv(1024).decode(FORMAT)
    conn.send(a.encode(FORMAT))
    
    b = conn.recv(1024).decode(FORMAT)
    conn.send(b.encode(FORMAT))
    
    message = "gia tri " + Type + ":" + solve(a,b,Type)
    
    conn.send(message.encode(FORMAT))
    
    print(message)
    
    sk.close()
        
    