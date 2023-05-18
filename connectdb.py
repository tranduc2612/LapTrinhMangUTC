# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:53:26 2023

@author: OSC
"""

import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSI\SQLEXPRESS;'
                      'Database=QLBanKinh;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM tKhachHang')

for i in cursor:
    print(i)