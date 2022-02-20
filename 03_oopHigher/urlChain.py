#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 19:54
# @Author   : Wayne Qi
# @FileName : urlChain.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
"要求对于Url().users('Michael').repos输出 users/Michael/repos"


# 这里用到定制函数__xxx__的方法，使得没有的attribute能够被查表解决
class Url(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Url("{0}/{1}".format(self._path, path))

    def __call__(self, path):
        return Url("{0}/{1}".format(self._path, path))  # 为了应对user("Michael")，本质上仍然是调用类

    def __str__(self):
        return self._path

    __repr__ = __str__  # 控制台打印的和str相同


print(Url().users("Michael").repos)

test = Url()

callable(Url) == True

callable(test) == False #这里说明已经实例化的对象不可调用

#模糊了类和函数的界限
