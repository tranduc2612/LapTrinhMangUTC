# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:13:26 2023

@author: OSC
"""
import socket
host = 'localhost'
port = 2024
FORMAT = 'utf-8'

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host, port))
    data = sk.recv(1024)
    print(data.decode(FORMAT))
    messageAcc = input("enter account: ")
    sk.send(messageAcc.encode(FORMAT))
    message = sk.recv(1024).decode()
    
    messagePass = input("enter password: ")
    sk.send(messagePass.encode(FORMAT));
    
    message = sk.recv(1024).decode()
    print(message)
    sk.close()
    