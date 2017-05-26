#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''
'''
Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，
以及两个基本的方法。
可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

构造方法： 
Lock()

实例方法： 
acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。 
release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
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