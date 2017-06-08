#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月7日

@author: Huoyunren
'''
import struct
import string
from pybase.socket.util.PacketUtil import PacketUtil
IP_DESC = ['version', 'header_length', 'service_type', 'packet_length', 'packet_split_flag',
         'packet_fragment_flag', 'packet_fragment_offset', 'TTL', 'protocol', 'header_crc'
         , 'src_ip', 'dest_ip'
        ]

def get_protocol(key):
    protocol_map = {
        1:'ICMP',
        2:'IGMP',
        3:'GGP',
        6:'TCP',
        17:'UDP'
        };
    if protocol_map.has_key(key):
        return protocol_map[key]
    return key


def get_ip(bts):
    return "%d.%d.%d.%d" % (bts[0], bts[1], bts[2], bts[3])

def show_ip_by_order(parse_header_dict):
    parse_header_desc = '{'
    for key in IP_DESC:
        parse_header_desc = parse_header_desc + key + ':' + str(parse_header_dict[key]) + ' '
    return parse_header_desc + "}"
def parse_packet(packet):
     '''
        45 
        0 
        0 5c 
        d f8 
        40 0 
        7d 06 
        92 a6 
        ac 16 3 ca 
        ac 10 1 d 
        ed 56 0 16 a5 dd b3 de 86 36 57 37 50 18 3f 66 41 73 0 0 9a 3f 28 80 11 3a 2d 73 50 f1 f3 9e 3a ed 7 a8 25 a0 73 51 5f bd cf a3 b9 59 1f 19 e2 5b 58 42 87 6a 67 98 88 78 54 d6 83 c8 a6 24 6b 1b 65 e5 ff af 82 44
     '''   
     spt = packet.split()
     sendMsg = []
     for temp_cwd in spt:
         sendMsg.append(string.atoi(temp_cwd, 16))
     c = bytearray(sendMsg) 
     total_packet_length = len(c)
     # print 'total_packet_length_input:%d' % total_packet_length
     ip_header = {}
     # 第一个字节高4 位 为版本号
     ip_header['version'] = (c[0] & 0xf0) >> 4  
     # 第一个字节 低4位 为首部长度 单位为 4字节 ，首部长度 ，如果不为 20 说明首部有可变字段
     # c[0]--c[19] 为IP 头部
     ip_header['header_length'] = (c[0] & 0x0f) * 4  
     # print 'total_packet_header_length_calc:%d' % ip_header['header_length']
     ip_header['service_type'] = c[1]
     
     # 一个 IP 数据包长度 最大 两个字节 65535 ，
     # 一个 以太网数据包 63 --1440，一个IP数据包可能分成多个
     # 以太网包发送     
     ip_header['packet_length'] = struct.unpack('>H', bytearray([c[2], c[3]]))[0]
     # print 'total_packet_length_calc:%d' % ip_header['packet_length']
     
     # 相同的标识字段的值使分片后的各数据报片最后能正确地重装成为原来的数据报.
     # 是否为同一个IP 数据报判断
     ip_header['packet_split_flag'] = struct.unpack('>H', bytearray([c[4], c[5]]))[0]
     # 3bit ?   DF MF
     #      n/a  1  1
     # 只有当 DF =0 才能分片，MF=1 表示还有分片数据 ，MF=0 表示是最后一个分片数据
     # 3bit =01,00
     # 1 不分 ，0 分包
     packet_fragment_flag = False
     if c[6] >> 6 == 0 :
         packet_fragment_flag = True
     ip_header['packet_fragment_flag'] = packet_fragment_flag 
     # 取低13 位 ，单位为 8 字节
     ip_header['packet_fragment_offset'] = (struct.unpack('>H', bytearray([c[6], c[7]]))[0] & 0x1fff) * 8
     # 单位秒
     ip_header['TTL'] = c[8]
     
     # 运输的协议
     ip_header['protocol'] = get_protocol(c[9])
     # header_crc 首部校验和,每经过一个路由器该值会发生变化
     ip_header['header_crc'] = struct.unpack('>H', bytearray([c[10], c[11]]))[0]
     ip_header['src_ip'] = get_ip([c[12], c[13], c[14], c[15]])
     # 20 字节头部解析完成
     ip_header['dest_ip'] = get_ip([c[16], c[17], c[18], c[19]])
     IP = {}
     IP['header_parse'] = ip_header
     IP['body'] = body = c[20:]
     IP['header'] = c[0:20]
     return IP

if __name__ == '__main__':
        packet_header_str = '45 00 00 5c 0d f8 40 00 7d 06 92 a6 ac 16 03 ca ac 10 01 0d'
        packet_body_str = 'ed 56 0 16 a5 dd b3 de 86 36 57 37 50 18 3f 66 41 73 0 0 9a 3f 28 80 11 3a 2d 73 50 f1 f3 9e 3a ed 7 a8 25 a0 73 51 5f bd cf a3 b9 59 1f 19 e2 5b 58 42 87 6a 67 98 88 78 54 d6 83 c8 a6 24 6b 1b 65 e5 ff af 82 44'
        parse_packet = parse_packet(packet_header_str + ' ' + packet_body_str)
        ip_header_parse = parse_packet['header_parse']
        print '=========header========'
        print show_ip_by_order(ip_header_parse)
        print  PacketUtil.show_hex_raw(parse_packet['header'])   
        print  PacketUtil.show_hex_raw(parse_packet['body'])
           
