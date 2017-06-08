#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月8日

@author: Huoyunren
'''
import socket
import struct
import platform

IP_DESC = ['version', 'header_length', 'service_type', 'packet_length', 'packet_split_flag',
         'packet_fragment_flag', 'packet_fragment_offset', 'TTL', 'protocol', 'header_crc'
         , 'src_ip', 'dest_ip'
        ]

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

def show_hex_raw(data):
        hex_str = ''
        if isinstance(data, str):
            for c in data:
                if ord(c) < 16:
                    hex_str = hex_str + '0' + (hex(ord(c))[2:]).upper() + ' ' 
                else:
                    hex_str = hex_str + (hex(ord(c))[2:]).upper() + ' ' 
        elif isinstance(data, bytearray):
            for c in data:
                if c < 16:
                    hex_str = hex_str + '0' + (hex(c)[2:]).upper() + ' ' 
                else:
                    hex_str = hex_str + (hex(c)[2:]).upper() + ' '  
        return  hex_str
    
def show_dict_by_order(dict_, desc):
    parse_header_desc = '{'
    for key in desc:
        parse_header_desc = parse_header_desc + key + ':' + str(dict_[key]) + ' '
    return parse_header_desc + "}"

def bytes_str(list_v):
        str_v = ''
        for c in list_v:
            str_v = str_v + chr(c)
        return  str_v

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

def ip_parser(packet):
    c = packet
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
    ip_header['packet_length'] = struct.unpack('>H', bytes_str([c[2], c[3]]))[0]
     # print 'total_packet_length_calc:%d' % ip_header['packet_length']
     
     # 相同的标识字段的值使分片后的各数据报片最后能正确地重装成为原来的数据报.
     # 是否为同一个IP 数据报判断
    ip_header['packet_split_flag'] = struct.unpack('>H', bytes_str([c[4], c[5]]))[0]
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
    ip_header['packet_fragment_offset'] = (struct.unpack('>H', bytes_str([c[6], c[7]]))[0] & 0x1fff) * 8
     # 单位秒
    ip_header['TTL'] = c[8]
     
     # 运输的协议
    ip_header['protocol'] = get_protocol(c[9])
     # header_crc 首部校验和,每经过一个路由器该值会发生变化
    ip_header['header_crc'] = struct.unpack('>H', bytes_str([c[10], c[11]]))[0]
    
    ip_header['src_ip'] = get_ip([c[12], c[13], c[14], c[15]])
     # 20 字节头部解析完成
    ip_header['dest_ip'] = get_ip([c[16], c[17], c[18], c[19]])
    IP = {}
    IP['header_parse'] = ip_header
    IP['body'] = body = c[20:]
    IP['header'] = c[0:20]
    return IP

def get_tcp_flag(flag):
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
    
def tcp_parse(packet):
    tcp_header_parse = {}
    tcp_header_parse[TCP_HEADER_DESC[0]] = struct.unpack('>H', bytes_str([packet[0], packet[1]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[1]] = struct.unpack('>H', bytes_str([packet[2], packet[3]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[2]] = struct.unpack('>L', bytes_str([packet[4], packet[5], packet[6], packet[7]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[3]] = struct.unpack('>L', bytes_str([packet[8], packet[9], packet[10], packet[11]]))[0]
    header_length = struct.unpack('>H', bytes_str([packet[12], packet[13]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[4]] = (header_length >> 12) * 4 
    tcp_header_parse[TCP_HEADER_DESC[5]] = (header_length & 0x0fc0) >> 6
    tcp_header_parse[TCP_HEADER_DESC[6]] = get_tcp_flag(header_length & 0x3f)
    tcp_header_parse[TCP_HEADER_DESC[7]] = struct.unpack('>H', bytes_str([packet[14], packet[15]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[8]] = struct.unpack('>H', bytes_str([packet[16], packet[17]]))[0]
    tcp_header_parse[TCP_HEADER_DESC[9]] = struct.unpack('>H', bytes_str([packet[18], packet[19]]))[0]
    tcp = {'header_parse':tcp_header_parse}
    tcp['header'] = packet[0:20]
    tcp['body'] = packet[20:]
    tcp['raw'] = packet
    return tcp;   
    
    
def start_dump():
    sock = None
    if platform.system() == 'Windows':
        # 获取所有IP 数据
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
        sock.bind((socket.gethostname(), 0))
        # Include IP headers
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # receive all packages
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        while True:
            packet = sock.recvfrom(65535)[0]
            if len(packet) == 0:
                sock.close()
                break
            ip_dict = ip_parser(bytearray(packet))
            ip_header_dict = ip_dict['header_parse'] 
            print show_dict_by_order(dict_=ip_header_dict, desc=IP_DESC)
            if ip_header_dict['protocol'] == 'TCP':  
                tcp_dict = tcp_parse(ip_dict['body'])
                tcp_header_dict = tcp_dict['header_parse']
                print '   tcp-----' + show_dict_by_order(dict_=tcp_header_dict, desc=TCP_HEADER_DESC)
    else:
        # 获取IP 层数据
        # sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        # 获取以太网数据链路层数据
        sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
        while True:
            packet = sock.recvfrom(65535)[0]
            if len(packet) == 0:
                sock.close()
                break
            print show_hex_raw(packet)

if __name__ == '__main__':
    start_dump()