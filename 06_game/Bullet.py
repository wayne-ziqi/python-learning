#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 20:19
# @Author   : Wayne Qi
# @FileName : Bullet.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

'All kinds of Bullet'

from BasicObj import Bullet

class BulletHero(Bullet):
    def __init__(self, Owner, window):
        super(BulletHero, self).__init__(Owner, window, 'BulletHero', 4, 1, 'images/bullet1.png')

    def exec(self):
        self.fly([0, -1])


class BulletEnemy(Bullet):
    def __init__(self, Owner, window):
        super(BulletEnemy, self).__init__(Owner, window, 'BulletEnemy', 1, 1, 'images/bullet2.png')

    def exec(self):
        self.fly([0, 1])


class BulletList(object):

    def __init__(self, Owner, window):
        self._list = []
        self._tick = 0

        self._owner = Owner
        if Owner.type() == 'Hero':
            self._delay = 10
        elif Owner.type() == 'Enemy3':
            self._delay = 100
        else:
            raise ("no type %s"%self.type())
        self._window = window

    def __len__(self):
        return len(self._list)

    def add_bullet(self):

        if self._owner.type() == 'Hero':
            self._list.append(BulletHero(self._owner, self._window))

        elif self._owner.type() == 'Enemy2' or self._owner.type() == 'Enemy3':
            self._list.append(BulletEnemy(self._owner, self._window))

    def update(self):
        for i in range(len(self._list) - 1, -1, -1):
            if self._list[i] and self._list[i].erasable():
                del self._list[i]
        for i in range(len(self._list)):
            self._list[i].update()

    def bullet_addable(self):
        self._tick += 1
        if self._tick >= self._delay:
            self._tick = 0
            return True
        else:
            return False

    def Bullet_generate(self):
        if self.bullet_addable():
            self.add_bullet()

    def Bullet_exec(self):
        for bullet in self._list:
            bullet.exec()