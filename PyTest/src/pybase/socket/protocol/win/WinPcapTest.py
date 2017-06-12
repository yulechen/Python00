#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月12日

@author: Huoyunren
'''
from winpcapy import WinPcapUtils
from winpcapy import WinPcapDevices
from pybase.socket.protocol import dump


def packet_callback(win_pcap, param, header, pkt_data):
#    print type(pkt_data)
    dump.parse(bytearray(pkt_data))
    # print pkt_data
    # Assuming IP (for real parsing use modules like dpkt)
    # ip_frame = pkt_data[14:]
    # Parse ips
    # src_ip = ".".join([str(ord(b)) for b in ip_frame[0xc:0x10]])
    # dst_ip = ".".join([str(ord(b)) for b in ip_frame[0x10:0x14]])
    # print("%s -> %s" % (src_ip, dst_ip))

def list_device():
    with WinPcapDevices() as devices:
        for device in devices:
            print device.name, device.description, device.flags , device.addresses.contents.netmask.contents.sa_family


if __name__ == '__main__':
    # WinPcapUtils.capture_on_and_print("*Realtek*")
    WinPcapUtils.capture_on("*Realtek*", packet_callback)
