#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/21 21:17
# @Author   : Wayne Qi
# @FileName : process.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

# import os
# print("Process {0} start...".format(os.getpid()))
# pid = os.fork()
# #子进程返回0
# if pid == 0:
#     print("child ({0}), parent ({1})".format(os.getpid(), os.getpid()))
# else:
#     print("{0} created child {1}".format(os.getpid(), pid))

# fork只能在posix内核使用

import os

# 子进程要执行的代码
def process1(name):
    print("run process {0}, process number {1}".format(name, os.getpid()))


# if __name__ == '__main__':

