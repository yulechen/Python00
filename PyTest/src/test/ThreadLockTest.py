#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年11月9日

@author: Huoyunren
'''

import thread, time, random
count = 0
lock = thread.allocate_lock()  # 创建一个琐对象
def threadTest():
    global count, lock
    lock.acquire()  # 获取琐
 
    for i in xrange(10000):
        count += 1
 
    lock.release()  # 释放琐
for i in xrange(10):
    thread.start_new_thread(threadTest, ())
time.sleep(3)
print count

