# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:32:41 2023

@author: OSC
"""

import socket
import calendar
host = 'localhost'
port = 2024
FORMAT = 'utf-8'

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sk.bind((host,port))
    
    sk.listen()
    
    print("listening client ...")
    conn,adress = sk.accept()
    data = 'hello client'
    
    conn.sendall(data.encode(FORMAT))
    
    data = conn.recv(1024).decode(FORMAT)
    
    data = data.split("/")
    month = int(data[0])
    year = int(data[1])
    
    
    day = str(calendar.monthrange(year,month)[1])
    
    message = 'Ngay cua thang do la ' + day
    
    conn.sendall(message.encode(FORMAT))
    
    sk.close()
    
    