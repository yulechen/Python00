# !
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月4日

@author: Huoyunren
'''
import socket
import string

def main(ip, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    # print s.recv(1024)
    # strr = ''
    spt = content.split()
    
    sendMsg = []
    for temp_cwd in spt:
      sendMsg.append(string.atoi(temp_cwd, 16)) 
    c = bytearray(sendMsg);
    s.send(c)
    s.close()
    print 'ok'
if __name__ == '__main__':
  main('iot.chinawayltd.com', 4568, '7E 01 02 00 07 01 40 02 02 00 69 1D E5 68 75 69 74 6F 6E 67 B2 7E')
