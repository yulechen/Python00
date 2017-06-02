#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月2日

@author: Huoyunren
'''
from io import StringIO
f = StringIO()
f.write('hello', 'utf-8')
f.write(' ')
f.write('world!')
print (f.getvalue('utf-8'))
