#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 20:19
# @Author   : Wayne Qi
# @FileName : bullet.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

'All kinds of Bullet'
from Plane import Plane

# logically, bullets are also a type of plane
class Bullet(Plane):

    def __init__(self, Owner, window, type,speed, blood,imgPath):
        self._owner = Owner
        super(Bullet, self).__init__(type, speed, Owner.head(), blood, window, imgPath)

    def fly(self, direction):
        self.move(direction, self._speed, True)
