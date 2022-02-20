#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 12:02
# @Author   : Wayne Qi
# @FileName : attr.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

class A(object):
    _nameA = 'class name A'
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def add(self, adder):
        self._value += adder

    def changeClassName(self, name = 'class name A'):
        self._nameA = name

    def className(self):
        return self._nameA

    def name(self):
        return self._name


if __name__ == '__main__':
    A1 = A('A1', 1)
    A2 = A('A2', 2)
    A1.changeClassName()
    A2.changeClassName('A2_changed')
    print()

