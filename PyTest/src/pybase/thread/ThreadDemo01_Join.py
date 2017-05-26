#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''


import threading
import time

def context(tJoin):
    print 'in threadContext.'
    tJoin.start()
    
    # 将阻塞tContext直到threadJoin终止。 等待另一个线程执行几秒，不传等待另一个线程执行完成。
    tJoin.join(1)
    
    # tJoin终止后继续执行。
    print 'out threadContext.'
 
def join():
    print 'in threadJoin.'
    time.sleep(3)
    print 'out threadJoin.'
 
tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))
 
tContext.start()