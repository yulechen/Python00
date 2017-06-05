#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月1日

@author: Huoyunren
'''

import requests
from io import BytesIO

# requset method
r = requests.get('https://github.com/timeline.json')
# print r.text 文本响应
result = bytearray(r.content);
print bytearray(r.content)  # 二进制响应内容
# print repr(r.raw)
# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")


# request param
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# r.url=http://httpbin.org/get?key2=value2&key1=value1

# print r.url
