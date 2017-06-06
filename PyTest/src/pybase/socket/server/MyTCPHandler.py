#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月6日

@author: Huoyunren
'''
from SocketServer import StreamRequestHandler

class MyTCPHandler(StreamRequestHandler):
    
    def handle(self):
            self.readlines = self.rfile.readlines(65537)
            print self.readlines
            if not self.readlines:
                for line in self.readlines:
                    print line
                   
    