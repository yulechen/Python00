#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月9日

@author: Huoyunren
'''
from pybase.socket.util.PacketUtil import PacketUtil


def  parse(packet):
  httpStr = PacketUtil.convertBytes2String(packet)
  requestline = httpStr.split('\r\n')
  print requestline
  words = requestline[0].split()
  print words
  http_request_line = {}
  http = {}
  if len(words) == 3:
    command, path, version = words
    if version[:5] != 'HTTP/':
        return http    
    http_request_line['method'] = command
    http_request_line['url'] = path
    http_request_line['version'] = version
    
    http_header = {};
    http['http_request_line'] = http_request_line
    
    http['header'] = http_header
    http['body'] = 'body'
  return http  
  
  
  
if __name__ == '__main__':
    bytes = PacketUtil.str2bytes('47 45 54 20 2F 64 61 70 2D 77 65 62 2F 70 61 67 65 2F 73 65 72 76 65 72 5F 6C 69 73 74 20 48 54 54 50 2F 31 2E 31 0D 0A 48 6F 73 74 3A 20 31 37 32 2E 31 36 2E 31 2E 31 36 3A 38 30 38 30 0D 0A 43 6F 6E 6E 65 63 74 69 6F 6E 3A 20 6B 65 65 70 2D 61 6C 69 76 65 0D 0A 43 61 63 68 65 2D 43 6F 6E 74 72 6F 6C 3A 20 6D 61 78 2D 61 67 65 3D 30 0D 0A 55 70 67 72 61 64 65 2D 49 6E 73 65 63 75 72 65 2D 52 65 71 75 65 73 74 73 3A 20 31 0D 0A 55 73 65 72 2D 41 67 65 6E 74 3A 20 4D 6F 7A 69 6C 6C 61 2F 35 2E 30 20 28 57 69 6E 64 6F 77 73 20 4E 54 20 36 2E 31 3B 20 57 69 6E 36 34 3B 20 78 36 34 29 20 41 70 70 6C 65 57 65 62 4B 69 74 2F 35 33 37 2E 33 36 20 28 4B 48 54 4D 4C 2C 20 6C 69 6B 65 20 47 65 63 6B 6F 29 20 43 68 72 6F 6D 65 2F 35 38 2E 30 2E 33 30 32 39 2E 31 31 30 20 53 61 66 61 72 69 2F 35 33 37 2E 33 36 0D 0A 41 63 63 65 70 74 3A 20 74 65 78 74 2F 68 74 6D 6C 2C 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 68 74 6D 6C 2B 78 6D 6C 2C 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 6D 6C 3B 71 3D 30 2E 39 2C 69 6D 61 67 65 2F 77 65 62 70 2C 2A 2F 2A 3B 71 3D 30 2E 38 0D 0A 41 63 63 65 70 74 2D 45 6E 63 6F 64 69 6E 67 3A 20 67 7A 69 70 2C 20 64 65 66 6C 61 74 65 2C 20 73 64 63 68 0D 0A 41 63 63 65 70 74 2D 4C 61 6E 67 75 61 67 65 3A 20 7A 68 2D 43 4E 2C 7A 68 3B 71 3D 30 2E 38 0D 0A 43 6F 6F 6B 69 65 3A 20 74 64 5F 63 6F 6F 6B 69 65 3D 31 38 34 34 36 37 34 34 30 37 31 32 31 32 32 33 32 36 38 34 3B 20 4A 53 45 53 53 49 4F 4E 49 44 3D 36 42 38 33 39 35 38 39 42 33 37 45 34 39 34 37 33 43 44 34 44 31 36 31 34 39 36 39 41 41 31 45 0D 0A 0D 0A')  
    # print bytes
    print parse(bytes) 
