#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月13日

@author: Huoyunren
'''

# arg a plain or long integer or a floating point number
# Return the absolute value of a number
print abs(-1), abs(1)

# 判断集合里面是否全部为 True
print all([1, 2, '']), all([1, 2, 3])

# 判断集合里面是否有一个为True
print any([1, 2, '']), any([1, 2, 3])

print bin(1), bin(10), type(bin(1))
# 一个整数 ，创建空的数组
# 一个整数（0-255） 集合 ，转换成byte 数组
print repr(bytearray(10)), repr(bytearray([1, 2]))

# 字符
print repr(bytearray(u'你好', 'gbk')), repr(bytearray('你好')), repr(bytearray('a'))


# 0-255 ascii
print chr(97), ord('a'), ord(u'你'), unichr(20320)
