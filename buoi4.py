# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:57:12 2023

@author: OSC
"""

import ftplib

ftp = ftplib.FTP('127.0.0.1')
ftp.login('ductm','123456')
data = []
ftp.dir(data.append)
#ftp.quit()

for i in data:
    print(i)


# upload file 
# =============================================================================
filename = 'upload2.txt'
ftp.encoding = 'utf-8'
with open(filename, 'rb') as f:
     ftp.storbinary(f'STOR {filename}', f)
# =============================================================================    


