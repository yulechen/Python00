#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月27日

@author: Huoyunren
'''
import socket
import errno
import platform

if platform.system() == 'Windows':
    EAGAIN = errno.WSAEWOULDBLOCK
else:
    EAGAIN = errno.EAGAIN

def _socketpair_compat():
    """TCP/IP socketpair including Windows support"""
    listensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    listensock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listensock.bind(("127.0.0.1", 22222))
    listensock.listen(1)

    iface, port = listensock.getsockname()
    print iface, port
    
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    sock1.setblocking(0)
    try:
        sock1.connect(("127.0.0.1", port))
    except socket.error as err:
        if err.errno != errno.EINPROGRESS and err.errno != errno.EWOULDBLOCK and err.errno != EAGAIN:
            raise
    sock2, address = listensock.accept()
    sock2.setblocking(0)
    listensock.close()
    return (sock1, sock2)

if __name__ == '__main__':
    sock1, sock2 = _socketpair_compat()
    print sock1
    print sock2
