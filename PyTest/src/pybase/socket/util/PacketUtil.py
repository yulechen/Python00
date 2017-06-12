#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月8日

@author: Huoyunren
'''
import string

class PacketUtil:
    @staticmethod
    def show_hex_raw(data):
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
    
    @staticmethod
    def convertBytes2String(list_v):
        str_v = ''
        for c in list_v:
            str_v = str_v + chr(c)
        return  str_v
    
    @staticmethod
    def bytes2Str(list_v):
        return  bytearray(list_v)
    
    @staticmethod
    def str2bytes(hexStrs):
        spt = hexStrs.split()
        sendMsg = []
        for temp_cwd in spt:
            sendMsg.append(string.atoi(temp_cwd, 16))
        return  bytearray(sendMsg)