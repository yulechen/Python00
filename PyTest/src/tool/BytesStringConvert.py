#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月8日

@author: Huoyunren
'''
import struct

def showHexRaw(data):
    hexStr = ''
    if isinstance(data, str):
        for c in data:
            if ord(c) < 16:
              hexStr = hexStr + '0' + (hex(ord(c))[2:]).upper() + ' ' 
            else:
               hexStr = hexStr + (hex(ord(c))[2:]).upper() + ' ' 
    elif isinstance(data, bytearray):
        for c in data:
            if c < 16:
              hexStr = hexStr + '0' + (hex(c)[2:]).upper() + ' ' 
            else:
               hexStr = hexStr + (hex(c)[2:]).upper() + ' '  
    return  hexStr         
    
# integer to bytesarray
key = struct.pack('BBBBBBBB', 17, 24, 121, 1, 12, 222, 34, 76)
print type(key), str(key), showHexRaw(key)

key1 = bytearray(key);
print type(key1), str(key1), showHexRaw(key)


unkey = struct.unpack('BBBBBBBB', key)
print type(unkey), str(unkey)

unkey1 = struct.unpack('BBBBBBBB', key1)
print type(unkey1), str(unkey1)


def convertBytes2String(list_v):
    str_v = ''
    for c in list:
        str_v = str_v + chr(c)
    return  str_v

# 字面值 不能进行拼接操作
def convertBytes2String2(list_v):
    str_v_type = b''
    str_v = ''
    for c in list_v:
        str_v = str_v + '\\x' + str(c)
    print type(b'x22x33') , b'\x22\x33'
    print type(str_v_type + str_v)


unkey2 = struct.unpack('BBBBBBBB', convertBytes2String([17, 24, 121, 1, 12, 222, 34, 76]))
print type(unkey2), str(unkey2)   
        

# str_v = 'y�"L'
# str_v_decode_bytes = str_v.encode('utf-8')
# print type(str_v_decode_bytes), showHexRaw(str_v_decode_bytes)


