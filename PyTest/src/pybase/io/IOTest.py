#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月2日

@author: Huoyunren
'''

def readFile(fileName):
    with open(fileName, 'r') as f:
        print f.read()

def readFile1(fileName):
    with open(fileName, 'r') as f:
        for line in f:
            print 'line_' + line
            
def readFile2(fileName):
    with open(fileName, 'r') as f:
        while True:
            line = f.read(10)
            bl = bytearray(line)
            for b in bl:
                print hex(b)
            # print line
            break
            if not line:
                break
            

def readBFile(fileName):
    with open(fileName, 'rb') as f:
        while True:
            line = f.read(10)
            if not line:
                break;
            print line

# fileName = 'D:/GitReps/Github\Python00/PyTest/src/test1.py'  # 文本文件
fileName = 'D:/GitReps/Github\Python00/PyTest/src/test1.pyc'  # 二进制文件

# readFile(fileName)
# readFile2(fileName)
readFile2(fileName)
