# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:31:44 2023

@author: OSC
"""
import socket
import os
from _thread import *
sk = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    sk.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
sk.listen(5)

def multi_threaded_client(client_sk):
    client_sk.send(str.encode('Server is working:'))
    while True:
        MessCount = 0
        data = client_sk.recv(2048)
        MessCount += 1
        response = 'Server message: ' + data.decode('utf-8')
        if not data or data == 'bye':
            break
        client_sk.sendall(str.encode(response))
    client_sk.close()
    print('Message count: ' + MessCount)
    client_sk.sendall(MessCount.encode('utf-8'))
    global ThreadCount
    ThreadCount = ThreadCount-1
            
while True:
    Client_sk, address = sk.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client_sk, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
sk.close()
