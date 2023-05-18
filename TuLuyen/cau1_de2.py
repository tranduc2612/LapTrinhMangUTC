# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:23:02 2023

@author: OSC
"""

from urllib.request import urlopen    
#import urllib.error    
from urllib.request import Request

if __name__ == '__main__':
    #tao doi tuong request
    req = Request("http://www.google.com")
    
    req.add_header('Accept-Encoding','gzip')
    r = urlopen(req)
    # print(r.read())
    print(r.status)    
    print(r.getheaders())
