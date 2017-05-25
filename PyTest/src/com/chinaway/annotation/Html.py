#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月25日

@author: Huoyunren
'''
# 当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值

def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"
        return wrapped
    return real_decorator
 
@makeHtmlTag(tag="b", css_class="bold_css")
# @makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"

print hello()
