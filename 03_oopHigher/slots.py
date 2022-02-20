#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 15:35
# @Author   : Wayne Qi
# @FileName : slots.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

class Student(object):
    pass

s = Student()
s._name = 'Michael'
print(s._name)

def set_age(self, age):
    self._age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s._age)