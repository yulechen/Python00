#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月8日

@author: Huoyunren
'''
#  TCP 首部与IP 首部一样都是 20 个字节 ，TCP 可变首部 最大值为 40 字节
#  TCP 首部最大为 60字节
import struct
from pybase.socket.util.PacketUtil import PacketUtil
TCP_HEADER_DESC = (
                'src_port',  # 16 位 max 65535
                'dest_port',  #  16 位 max 65535
                'seq',  # 32 位
                'ack',  # 32 位
                'header_length',  # ４位　，单位4字节 ，max =60
                'reverse',  # 6位 保留
                'flag' ,  # 6位 URG|ACK|PSH|RST|SYN|FIN
                'win',  # 16 位，max 65535
                'crc',  # 16 位 ，检验和字段检验的范围包括首部和数据这两部分
                'urg'  # 16 位 紧急指针 紧急指针在URG=1时才有效
                 # ‘option’ 长度可变，最长可达40字节
                 )
def get_flag(flag):
    flag_str = ''
    if (flag >> 5) & 0x01 == 1 :
        flag_str = flag_str + 'URG' 
    if (flag >> 4) & 0x01 == 1 :
        flag_str = flag_str + 'ACK' 
    if (flag >> 3) & 0x01 == 1 :
        flag_str = flag_str + 'PSH' 
    if (flag >> 2) & 0x01 == 1 :
        flag_str = flag_str + 'RST'     
    if (flag >> 1) & 0x01 == 1 :
        flag_str = flag_str + 'SYN'     
    if flag & 0x01 == 1 :
        flag_str = flag_str + 'FIN'      
    return flag_str
 
def show_tcp_by_order(parse_header_dict):
    parse_header_desc = '{'
    for key in TCP_HEADER_DESC:
        parse_header_desc = parse_header_desc + key + ':' + str(parse_header_dict[key]) + ' '
    return parse_header_desc + "}"
      
def parse_packet(packet):
    '''
    @param packet:  bytearray
    @return: dict keys=[header_parse,header,raw,body]
   '''
    try:
        print len(packet)
        tcp_header_parse = {}
        tcp_header_parse[TCP_HEADER_DESC[0]] = struct.unpack('>H', bytearray([packet[0], packet[1]]))[0]
        tcp_header_parse[TCP_HEADER_DESC[1]] = struct.unpack('>H', bytearray([packet[2], packet[3]]))[0]
        tcp_header_parse[TCP_HEADER_DESC[2]] = struct.unpack('>L', bytearray([packet[4], packet[5], packet[6], packet[7]]))[0]
        tcp_header_parse[TCP_HEADER_DESC[3]] = struct.unpack('>L', bytearray([packet[8], packet[9], packet[10], packet[11]]))[0]
        header_length = struct.unpack('>H', bytearray([packet[12], packet[13]]))[0]
        print header_length
        tcp_header_parse[TCP_HEADER_DESC[4]] = (header_length >> 12) * 4 
        tcp_header_parse[TCP_HEADER_DESC[5]] = (header_length & 0x0fc0) >> 6
        tcp_header_parse[TCP_HEADER_DESC[6]] = get_flag(header_length & 0x3f)
        tcp_header_parse[TCP_HEADER_DESC[7]] = struct.unpack('>H', bytearray([packet[14], packet[15]]))[0]
        tcp_header_parse[TCP_HEADER_DESC[8]] = struct.unpack('>H', bytearray([packet[16], packet[17]]))[0]
        tcp_header_parse[TCP_HEADER_DESC[9]] = struct.unpack('>H', bytearray([packet[18], packet[19]]))[0]
        tcp = {'header_parse':tcp_header_parse}
        tcp['header'] = packet[0:20]
        tcp['body'] = packet[20:]
        tcp['raw'] = packet
        return tcp
    except IndexError as  e:
        print tcp_header_parse
        print e   

if __name__ == '__main__':
    packet_body_str = 'C3 FA 1F 90 56 46 5F CC B4 85 E9 CC 50 18 40 29 5F 1D 00 00 47 45 54 20 2F 64 61 70 2D 77 65 62 2F 70 61 67 65 2F 73 65 72 76 65 72 5F 6C 69 73 74 20 48 54 54 50 2F 31 2E 31 0D 0A 48 6F 73 74 3A 20 31 37 32 2E 31 36 2E 31 2E 31 36 3A 38 30 38 30 0D 0A 43 6F 6E 6E 65 63 74 69 6F 6E 3A 20 6B 65 65 70 2D 61 6C 69 76 65 0D 0A 43 61 63 68 65 2D 43 6F 6E 74 72 6F 6C 3A 20 6D 61 78 2D 61 67 65 3D 30 0D 0A 55 70 67 72 61 64 65 2D 49 6E 73 65 63 75 72 65 2D 52 65 71 75 65 73 74 73 3A 20 31 0D 0A 55 73 65 72 2D 41 67 65 6E 74 3A 20 4D 6F 7A 69 6C 6C 61 2F 35 2E 30 20 28 57 69 6E 64 6F 77 73 20 4E 54 20 36 2E 31 3B 20 57 69 6E 36 34 3B 20 78 36 34 29 20 41 70 70 6C 65 57 65 62 4B 69 74 2F 35 33 37 2E 33 36 20 28 4B 48 54 4D 4C 2C 20 6C 69 6B 65 20 47 65 63 6B 6F 29 20 43 68 72 6F 6D 65 2F 35 38 2E 30 2E 33 30 32 39 2E 31 31 30 20 53 61 66 61 72 69 2F 35 33 37 2E 33 36 0D 0A 41 63 63 65 70 74 3A 20 74 65 78 74 2F 68 74 6D 6C 2C 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 68 74 6D 6C 2B 78 6D 6C 2C 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 6D 6C 3B 71 3D 30 2E 39 2C 69 6D 61 67 65 2F 77 65 62 70 2C 2A 2F 2A 3B 71 3D 30 2E 38 0D 0A 41 63 63 65 70 74 2D 45 6E 63 6F 64 69 6E 67 3A 20 67 7A 69 70 2C 20 64 65 66 6C 61 74 65 2C 20 73 64 63 68 0D 0A 41 63 63 65 70 74 2D 4C 61 6E 67 75 61 67 65 3A 20 7A 68 2D 43 4E 2C 7A 68 3B 71 3D 30 2E 38 0D 0A 43 6F 6F 6B 69 65 3A 20 74 64 5F 63 6F 6F 6B 69 65 3D 31 38 34 34 36 37 34 34 30 37 31 32 31 32 32 33 32 36 38 34 3B 20 4A 53 45 53 53 49 4F 4E 49 44 3D 36 42 38 33 39 35 38 39 42 33 37 45 34 39 34 37 33 43 44 34 44 31 36 31 34 39 36 39 41 41 31 45 0D 0A 0D 0A'
    packet = PacketUtil.str2bytes(packet_body_str)
    tcp_data = parse_packet(packet)  
    print show_tcp_by_order(tcp_data['header_parse'])
    print PacketUtil.show_hex_raw(tcp_data['body'])
    print PacketUtil.show_hex_raw(tcp_data['header'])
    print PacketUtil.show_hex_raw(tcp_data['raw'])
       
    
