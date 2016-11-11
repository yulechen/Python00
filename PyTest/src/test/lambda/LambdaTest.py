#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月11日

@author: Huoyunren
'''
'''
 匿名函数 ，
'''

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print f(1);

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print pairs