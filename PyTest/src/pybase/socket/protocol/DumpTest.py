#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月9日

@author: Huoyunren
'''
import dump
from pybase.socket.util.PacketUtil import PacketUtil

if __name__ == '__main__':
    frame_str_hex = '00 16 3E 00 07 39 \
    EE FF FF FF FF FF \
    08 00 \
    45 00 00 28 7F DF 40 00 7D 06 \
    20 F3 AC 16 03 CA AC 10 01 0D ED 56 00 16 A5 E3 90 EE 86 40 95 07 50 10 3E E7 \
    D4 68 00 00'
    frame_bytes = PacketUtil.str2bytes(frame_str_hex)
    dump.parse(frame_bytes)