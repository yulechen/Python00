#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''
from com.chinaway.exception.Exceptions import InputError

class ExceptionTest:
    
    def catchException(self):
        while True:
            try:
                x = int(raw_input("Please enter a number: "))
                print x
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
                
                
    def raseException(self):
        raise Exception
    
    def raseMyException(self):
        raise InputError("a", "input Error")            
