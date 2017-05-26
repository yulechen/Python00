#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''
'''
Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。

构造方法： 
Timer(interval, function, args=[], kwargs={}) 
interval: 指定的时间 
function: 要执行的方法 
args/kwargs: 方法的参数
'''

import threading

def func():
    print 'hello timer!'
 
timer = threading.Timer(5, func)
timer.start()