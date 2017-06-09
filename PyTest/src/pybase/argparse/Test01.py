#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月9日

@author: Huoyunren
'''

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
# -a -bval -c 3
args = parser.parse_args(['-a', '-bval', '-c', '3'])
print args.b, args.c
