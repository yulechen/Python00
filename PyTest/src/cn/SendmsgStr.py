# !
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月4日

@author: Huoyunren
'''
import socket

def main(ip, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port)) 
    s.send(content)
    data = s.recv(1024)
    print data
    s.close()
    print 'ok'
if __name__ == '__main__':
  main('172.16.1.16', 4569, 'id=1212131415，name=传感器，value=26，x=123，y=234，z=22')
