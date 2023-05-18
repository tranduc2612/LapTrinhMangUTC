# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:40:58 2023

@author: OSC
"""

import socket
PORT = 2024
HOST = 'localhost'
FORMAT = 'utf-8'

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind((HOST,PORT))
    sk.listen()
    print('listen on client ...')
    
    conn,adress = sk.accept()
    data = 'hello client'
    conn.send(data.encode(FORMAT))
    
    while True:
        data = conn.recv(1024).decode(FORMAT)
        
        if(data == 'bye'):
            print('client said bye')
            conn.send(data.encode(FORMAT))
            sk.close()
            break;
        
        print(data)
        message = input("send client something: ")
        if(message == 'bye'):
            sk.close()
            
        conn.send(message.encode(FORMAT))
        
    