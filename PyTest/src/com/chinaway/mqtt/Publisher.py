# -*- coding: UTF-8 -*-
'''
Created on 2016年11月8日

@author: Huoyunren
'''
import paho.mqtt.publish as publish
import time
t = u"emqtt/test/single/1"
i = 0;
while True:
 i = i + 1
 publish.single(t, u"hello mqtt " + str(i), hostname="172.16.1.17", auth={'username':'radmin', 'password':'radmin'})
 print 'publish message...'
 time.sleep(1)
print 'done'
