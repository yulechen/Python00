#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月11日
Pack codes 
"H" and "I" represent two and four byte unsigned numbers respectively. 
The "<" indicates that they are standard size and in little-endian byte order
@author: Huoyunren
'''
import struct

data = open('myfile.zip', 'rb').read()
start = 0
for i in range(3):  # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start + extra_size]
    print filename, hex(crc32), comp_size, uncomp_size

    start += extra_size + comp_size  # skip to the next header
