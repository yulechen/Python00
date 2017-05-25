#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月25日

@author: Huoyunren
'''
def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

@hello
def foo():
    print "i am foo"
# foo =hell(foo)
foo()