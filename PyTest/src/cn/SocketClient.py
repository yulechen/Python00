# !
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月4日

@author: Huoyunren
'''
import socket
import time

def main(ip, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port)) 
    s.send(content)
   # data = s.recv(1024)
   # print data
   # s.close()
    print 'ok'
    time.sleep(10000)
if __name__ == '__main__':
 # main('172.16.1.16', 4569, 'id=1212131415，name=传感器，value=26，x=123，y=234，z=22')
 # main('172.16.1.16', 4571, 'AT+GTSRI=gv55,3,,1,172.16.1.16,4571,192.0.0.0,0,,5,0,1,1,,,FFFF$')
 # main('172.16.1.16', 4572, 'AT+GTSRI=gv55,3,,1,172.16.1.16,4571,192.0.0.0,0,,5,0,1,1,,,FFFF$')
 # main('172.16.1.16', 4571, '+HBD=gv55,3,,1,172.16.1.16,4571,192.0.0.0,0,,5,0,1,1,,,FFFF$')
 # main('172.16.1.16', 16666, '{+HBD=gv55,3,,1,172.16.1.16,4571,}{192.0.0.0,0,,5,0,1,1,,,FFFF$}')
  main('172.16.1.16', 4567, '{+HBD=gv55,3,,1,172.16.1.16,4571,}{192.0.0.0,0,,5,0,1,1,,,FFFF$}')
  # main('123.56.0.101', 4571, 'AT+GTSRI=gv55,3,,1,172.16.1.16,4571,192.0.0.0,0,,5,0,1,1,,,FFFF$')
 
