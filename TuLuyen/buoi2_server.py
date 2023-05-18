# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:51:56 2023

@author: OSC
"""

import socket
host = 'localhost'
port = 2024
FORMAT = 'utf8'

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host,port))
    sk.listen()
    
    print("listening client")
    
    conn, address = sk.accept();
    """
    Đoạn này là kết nối được với 1 client 
    """
    data = 'hello client'
    conn.send(data.encode(FORMAT))
    dataAcc = conn.recv(1024).decode(FORMAT)
    message = 'tai khoan hop le'
    conn.send(message.encode(FORMAT))
    
    dataPass = conn.recv(1024).decode(FORMAT)
    message = 'dang nhap thanh cong'
    conn.send(message.encode(FORMAT))
    
    sk.close()