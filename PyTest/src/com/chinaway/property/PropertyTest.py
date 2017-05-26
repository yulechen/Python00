#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''

class Person(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.__log = None
        self._log = None
    #----------------------------------------------------------------------
    @property
    def full_name(self):
        """
        Return the full name
        """
        return "%s %s" % (self.first_name, self.last_name)
    
    
    @property
    def  m(self):
        return self.__private_show
    
    @m.setter
    def  m(self, f):
        self.__private_show = f
    
    def  __private_show(self):    
        print "%s %s" % (self.first_name, self.last_name)
        
def f():
    print "change method  show ok"
        
person = Person("Mike", "Driscoll")
print person.full_name
if person._log is not None:  # private method
    person._log()
if person.__log is not None:  # private method
    person.__log()
person.m()
person.m = f
person.m()
