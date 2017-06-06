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
    a = s.recv(1024)
    print a 
    # while True:
    #   pass
    s.close()
    print 'ok'
if __name__ == '__main__':
   main('172.22.3.123', 4573, '2B 48 42 44 E1 1B 56 15 5D 02 04 59 57 08 07 E0 0B 11 0F 1C 28 76 3B B9 4F 0D 0A')
   # main('172.16.1.16', 4571, '2B 48 42 44 E1 1B 56 15 5D 02 04 59 57 08 07 E0 0B 11 0F 1C 28 76 3B B9 4F 0D 0A')
  # main('123.56.0.101', 4571, '2B 48 42 44 E1 1B 56 15 5D 02 04 59 57 08 07 E0 0B 11 0F 1C 28 76 3B B9 4F 0D 0A')
   main('123.56.0.101', 16601, '7E 09 02 04 3B 01 50 90 08 43 00 10 1A F1 1C FF 17 05 15 16 00 34 00 00 00 01 BE 40 A3 07 1E 57 AB 2A 58 44 31 2C 34 31 35 47 2C 30 33 2C 30 30 30 30 2C 30 30 33 31 2C 30 31 0A 00 B0 30 30 2C 6E 75 6C 6C 2C 34 37 23 E7 7E')
  # main('172.22.3.123', 2906, '7E 02 00 00 60 00 00 60 03 93 33 01 68 00 00 08 80 00 0C 00 01 01 DB 7F D0 07 3B 88 D8 00 1B 00 00 00 00 16 11 25 14 31 12 01 04 00 01 89 CA 02 02 00 00 03 02 00 00 25 04 00 00 00 00 2A 02 00 00 2B 04 00 13 00 00 30 01 03 31 01 02 32 01 00 09 0A 00 00 00 00 00 00 00 00 00 00 E1 0E 01 16 11 25 14 07 02 16 11 25 14 26 11 01 FF D1 7E')

