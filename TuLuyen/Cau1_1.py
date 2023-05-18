# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:22:19 2023

@author: OSC
"""

from urllib.request import urlopen    
#import urllib.error    
from urllib.request import Request

if __name__ == '__main__':
    #tao doi tuong request
    req = Request("http://www.debian.org")
    
    req.add_header('Accept-Encoding','gzip')
    r = urlopen(req)
    print(r.read())
    print(r.status)    
    print(r.getheaders())
    
    #try:
    #    r = urlopen('http://www.python.org')
     #   print(r.read())
      #  print(r.status)    
       # print(r.getheaders())
    #except urllib.error.HTTPError as e:
        #print(e.msg)