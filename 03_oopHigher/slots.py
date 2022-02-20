#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 15:35
# @Author   : Wayne Qi
# @FileName : slots.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

'探究类的slot功能'

####################
print("\ntest1\n")
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

##############################
print("\ntest2\n")
class StudentSlot(object):
    __slots__ = ('_name', '_age')

ss = StudentSlot()
ss._name = 'Michael'
ss._age = 25

class GraduateStudent(StudentSlot):
    pass

#slots不能限制子类
g = GraduateStudent()
g._score = 77
print("g's score is {0}".format(g._score))

def set_score(self, score):
    self._score = score

GraduateStudent.set_score = set_score #相当于存储了函数指针，不止给对象绑定方法，而写给类绑定方法

g.set_score(88)
print("g's score is {0}".format(g._score))

