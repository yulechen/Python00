# -*- coding: UTF-8 -*-
'''
Created on 2016年11月8日

@author: Huoyunren
'''
import paho.mqtt.publish as publish
t = u"emqtt/test/single/1"
publish.single(t, u"bôô", hostname="172.16.1.17", auth={'username':'radmin', 'password':'radmin'})
print 'done'
