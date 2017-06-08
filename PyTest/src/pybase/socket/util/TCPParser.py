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
    if flag >> 5 == 1 :
        flag_str = flag_str + 'URG' 
    if flag >> 4 == 1 :
        flag_str = flag_str + 'ACK' 
    if flag >> 3 == 1 :
        flag_str = flag_str + 'PSH' 
    if flag >> 2 == 1 :
        flag_str = flag_str + 'RST'     
    if flag >> 1 == 1 :
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
    
    tcp_header_parse = {}
    tcp_header_parse[TCP_HEADER_DESC[0]] = struct.unpack('>H', bytearray([packet[0], packet[1]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[1]] = struct.unpack('>H', bytearray([packet[2], packet[3]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[2]] = struct.unpack('>L', bytearray([packet[4], packet[5], packet[6], packet[7]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[3]] = struct.unpack('>L', bytearray([packet[8], packet[9], packet[10], packet[11]]))[0]
    header_length = struct.unpack('>H', bytearray([packet[12], packet[13]]))[0]
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
    return tcp;

if __name__ == '__main__':
    packet_body_str = 'ed 56 0 16 a5 dd b3 de 86 36 57 37 50 18 3f 66 41 73 0 0 9a 3f 28 80 11 3a 2d 73 50 f1 f3 9e 3a ed 7 a8 25 a0 73 51 5f bd cf a3 b9 59 1f 19 e2 5b 58 42 87 6a 67 98 88 78 54 d6 83 c8 a6 24 6b 1b 65 e5 ff af 82 44'
    packet = PacketUtil.str2bytes(packet_body_str)
    tcp_data = parse_packet(packet)  
    print show_tcp_by_order(tcp_data['header_parse'])
    print PacketUtil.show_hex_raw(tcp_data['body'])
    print PacketUtil.show_hex_raw(tcp_data['header'])
    print PacketUtil.show_hex_raw(tcp_data['raw'])
       
    
