#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月11日

@author: Huoyunren
'''
# There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce().
def f(x): return x % 3 == 0 or x % 5 == 0

print filter(f, range(2, 25))
print filter(lambda x:x % 3 == 0 or x % 5 == 0, range(2, 25))

def cube(x): return x * x * x
print map(cube, range(1, 11))

seq = range(8)
def addMap(x, y): return x + y
print map(addMap, seq, seq)

def addReduce(x, y): return x + y
print reduce(addReduce, range(1, 11))

def sum(seq):
 def add(x, y): return x + y
 return reduce(add, seq, 2)
print sum(range(1, 11))
 