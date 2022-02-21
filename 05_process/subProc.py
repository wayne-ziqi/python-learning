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

#父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了