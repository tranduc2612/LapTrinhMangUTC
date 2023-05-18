# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket

if __name__ == '__main__':
    hostname = socket.gethostname()
    print(hostname)
    ip_addr = socket.gethostbyname(hostname)
    print(ip_addr)
    print(socket.gethostbyname_ex('www.google.com'))
    print(socket.gethostbyaddr('8.8.8.8'))
    print(socket.getfqdn('www.google.com'))
    print(socket.getaddrinfo('www.google.com', None,0,socket.SOCK_STREAM))


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
        
        
from http.cookiejar import CookieJar
from urllib.request import build_opener,HTTPCookieProcessor
import datetime
if __name__ == '__main__':
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open('http://www.github.com')
    cookies = list(cookie_jar)
    print(len(cookies))
    print(cookies)
    print(cookies[0].name)
    print(cookies[0].value)
    print(cookies[0].expires)
    print(cookies[0].path)
    print(cookies[0].domain)
    print(cookies[0].secure)    
    print(datetime.datetime.fromtimestamp(cookies[0].expires))    
        
        