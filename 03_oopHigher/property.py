#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 17:06
# @Author   : Wayne Qi
# @FileName : property.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

class Student(object):
    def __init__(self, score=0):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        elif value < 0 and value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

s1 = Student(100)
s1._score = 50  #不好，虽然补全不会显示但是仍然不会做类型检查，必须调用 set函数才能检查
print(s1._score)

class StudentE (object):
    def __init__(self, value = 0):
        self.score = value

    @property   #把一个getter方法通过decorator变成属性（变量）,属性名为函数名
    def score(self):
        return self._score  #不能写成score否则会递归

    #如果不设置setter就相当于只读属性
    @score.setter   #该属性的设置函数
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        elif value < 0 and value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

s2 = StudentE(50)
s2.score = 70   #不能写_score，否则不会做类型检查
print(s2._score)
