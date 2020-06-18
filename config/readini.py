#coding:utf-8

import os
import configparser


filepath=r'C:\Users\John\eclipse-workspace\Console\src\com\config\test.ini'
    
con=configparser.ConfigParser()
con.read(filepath)
    
to_addrs=con.get('email','to_addrs')
sender = con.get('email', 'sender')
subject = con.get('email', 'subject')
smtpserver = con.get('email', 'smtpserver')
username = con.get('email', 'username')
password = con.get('email', 'password')

print(to_addrs)