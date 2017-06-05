#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月5日

@author: Huoyunren
'''
# struct Header
# 
# {
# 
#     unsigned short id;
# 
#     char[4] tag;
# 
#     unsigned int version;
# 
#     unsigned int count;
# 
# }

import struct

ids = 100  # unsigned short integer 2byte
tag = '1234'  # 4 字节
version = 1000  # 4byte
count = 1  # 4byte
ss = struct.pack("!H4s2I", ids, tag, version, count);  # 大端编码,
print  type(ss)
bytess = bytearray(ss);
print type(bytes)
for b in bytess :
    print hex(b)
    
print '-------'   
# ss = struct.pack("<H4s2I", ids, tag, version, count);  # 小端编码,



id1, tag1, version1, count1 = struct.unpack("!H4s2I", ss)
print id1, tag1, version1, count1