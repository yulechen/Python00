#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月9日

@author: Huoyunren
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo