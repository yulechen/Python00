#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月26日

@author: Huoyunren
'''
'''
3. threading
threading基于Java的线程模型设计。锁（Lock）和条件变量（Condition）在Java中是对象的基本行为
（每一个对象都自带了锁和条件变量），而在Python中则是独立的对象。Python Thread提供了Java Thread的行为的子集；
没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。Java Thread中的部分被Python实现了的静态方法在threading中以模块方法的形式提供。

threading 模块提供的常用方法： 
threading.currentThread(): 返回当前的线程变量。 
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading模块提供的类：  
Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local.
'''
import threading
import time
# 方法1：将要执行的方法作为参数传给Thread的构造方法
def func():
    while True: 
        time.sleep(1)
        print '[' + threading.current_thread().name + ']' + 'func() passed to Thread' 
 
t = threading.Thread(target=func)
t.start()
 
# 方法2：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            print '[' + threading.current_thread().name + ']' + 'MyThread extended from Thread' 
 
t = MyThread()
t.start()
