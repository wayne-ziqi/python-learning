#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/21 22:44
# @Author   : Wayne Qi
# @FileName : subProc.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

__author__ = 'wayne'

import subprocess

print("%s$ nslookup www.python.org" % __author__)
r = subprocess.call(["nslookup", "www.python.org"])
print("exit code :", r)
