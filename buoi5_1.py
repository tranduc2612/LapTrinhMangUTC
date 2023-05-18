# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:02:03 2023

@author: OSC
"""

import socket
import sys
if __name__ == '__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as e:
        print('fail to create socket')
        print(str(e))
        sys.exit()
    print('socket created')
    host = 'localhost'
    port = 9050
    sk.bind((host,port))
    print('Socket bind to %s port %s'%(host,port))
    sk.listen(5)
    print('waiting.....')
    while True:
        client_sk,client_addr = sk.accept()
        print('Client address', client_addr)
        client_sk.send('Hello client'.encode('utf-8'))
        client_sk.close()
        break
        if not data:
            break
        print(data.decode('utf-8'))
        client_sk