#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 12:02
# @Author   : Wayne Qi
# @FileName : attr.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

class A(object):
    _nameA = 'class name A' #对每个不同的对象都有一个单独的class name
    _count = 0
    def __init__(self, name, value):
        self._name = name
        self._value = value
        A._count += 1

    def add(self, adder):
        self._value += adder

    def changeClassName(self, name = 'class name A'):
        A._nameA = name #不能用self，应用自己的类名共享变量，相当于静态成员函数

    def className(self):
        return self._nameA

    def name(self):
        return self._name

    def countObj(self):
        return A._count




if __name__ == '__main__':
    A1 = A('A1', 1)
    A2 = A('A2', 2)
    A1.changeClassName("A1_changed")
    print("A1's name is {0}, A1's class name is {1}, A2's class name is {2}".format(A1.name(), A1.className(), A2.className()))
    A2.changeClassName('A2_changed')
    print("A1 class name: {0}, A2 class name: {1}, obj count is {2}".format(A1.className(), A2.className(), A1.countObj()))

