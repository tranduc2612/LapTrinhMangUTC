# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:43:54 2023

@author: OSC
"""


import socket
PORT = 2024
HOST = 'localhost'
FORMAT = 'utf-8'

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    
    while True:
       data = client.recv(1024).decode(FORMAT)
       print(data)
       if(data == 'bye'):
           print('client close')
           client.close()
           break;
       
       message = input('Send something to server: ')
       client.send(message.encode(FORMAT))
           
        