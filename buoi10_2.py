# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:04:21 2023

@author: OSC
"""

import socket

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = 'hello server'
    sk.connect(data.encode(),('127.0.0.1',9050))
    data, server_addf = sk.recvfrom(1024)
    print(data.decode('utf-8'))    
    