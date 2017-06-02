#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月2日

@author: Huoyunren
'''

# 在 Python 中创建字节与字符串类似，只不过需要在引号外面加一个前缀b： ASCII 码
print(b"Python")
python = (b'P' b'y' b"t" b'o' b'n')
print(python)
print(b"Python"[0])

# 答案就是用特殊的转义符号\x+十六进制数字 
print(b'\xff'[0])
print(b'\x24')

print(bytes([24]))
print(bytes([36, 36, 36]))  # 记住字节类型是一个序列


# print(bytes.fromhex("7b 7d"))

# 逆运算
# print(b'{ }'.hex())

# int(b' '.hex(), base=16)

ba = bytearray(b'hello')
for i in ba:
    print hex(i)
print(ba)


def example(express, result=None):  
    if result == None:  
        result = eval(express)  
    print(express, ' ==> ', result)  
  
  
