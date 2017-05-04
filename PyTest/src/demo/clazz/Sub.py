# -*- coding: UTF-8 -*-
'''
Created on 2017年5月3日

@author: Huoyunren
'''
from demo.clazz.Parent import Parent


class Sub(Parent):
    '''
    classdocs
    '''      
# def __init__(self):
#     print 'sub cons'
          
    def b(self):
        print 'sub b '    
        
if __name__ == '__main__':
    s = Sub()
    s.mainM()
