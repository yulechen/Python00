# -*- coding: UTF-8 -*-
'''
Created on 2017年5月3日

@author: Huoyunren
'''

class Parent:
    '''
    Class
    '''


    def __init__(self):
        '''
        构造函数
        '''
        self.name = 'a'
        self.mname = 'b'
        print 'Parent constr method..'
        
        
    def mainM(self):
        result = getattr(self, 'b');
        result();
        print dir(self)
    
