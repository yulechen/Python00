#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月9日

@author: Huoyunren
'''
from pybase.socket.util.PacketUtil import PacketUtil
import struct


ETH_DESC = ('dest_mac', 'src_mac', 'type', 'crc')

def bytes_str(list_v):
        str_v = ''
        for c in list_v:
            str_v = str_v + chr(c)
        return  str_v
        
def get_hex_format(number):
    if number < 16:
        return '0' + (hex(number)[2:]).upper()
    else:
        return (hex(number)[2:]).upper()
                   
def get_eth_mac(mac_bytes):
    return "%s-%s-%s-%s-%s-%s" % (get_hex_format(mac_bytes[0]), get_hex_format(mac_bytes[1]),
                            get_hex_format(mac_bytes[2]), get_hex_format(mac_bytes[3]),
                            get_hex_format(mac_bytes[4]), get_hex_format(mac_bytes[5]))

def get_eth_type(key):
    type_map = {
        0x0800:'IP',
        0x0806:'ARP',
        0x8035:'RARP'
        };
    if type_map.has_key(key):
        return type_map[key]
    return key

def parser(frame_bytes):
    '''00 16 3E 00 07 39 EE FF FF FF FF FF 08 00 45 00 00 3C 89 61 40 00 40 06 57 1D 
       AC 10 01 10 AC 10 01 0D 05 82 08 85 77 26 A6 86 00 00 00 00 A0 02 
      39 08 DB F9 00 00 02 04 05 B4 04 02 08 0A 7D 25 2F E7 00 00 00 00 01 03 03 07
    '''
    eth = {}
    eth_parse_header = {};
    eth_parse_header[ETH_DESC[0]] = get_eth_mac(frame_bytes[0:6])
    eth_parse_header[ETH_DESC[1]] = get_eth_mac(frame_bytes[6:12])
    type_key = struct.unpack('>H', bytes_str([frame_bytes[12], frame_bytes[13]]))[0]
    eth_parse_header[ETH_DESC[2]] = get_eth_type(type_key)
    eth['body'] = frame_bytes[14:-4]
    eth_parse_header[ETH_DESC[3]] = struct.unpack('>L', bytes_str([frame_bytes[-4], frame_bytes[-3], frame_bytes[-2], frame_bytes[-1]]))[0]
    eth['header_parse'] = eth_parse_header
    return eth;
if __name__ == '__main__':
    frame_str_hex = '00 16 3E 00 07 39 EE FF FF FF FF FF 08 00 45 00 00 3C 89 61 40 00 40 \
    06 57 1D AC 10 01 10 AC 10 01 0D 05 82 08 85 77 26 A6 86 00 00 00 00 A0 02 39 08 DB F9 \
    00 00 02 04 05 B4 04 02 08 0A 7D 25 2F E7 00 00 00 00 01 03 03 07'
    frame_bytes = PacketUtil.str2bytes(frame_str_hex)
    print parser(frame_bytes)
