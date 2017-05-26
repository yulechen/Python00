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

local = threading.local()
local.tname = 'main'
 
def func():
    local.tname = 'notmain'
    print local.tname
 
t1 = threading.Thread(target=func)
t1.start()
t1.join()
 
print local.tname