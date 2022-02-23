#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/23 13:49
# @Author   : Wayne Qi
# @FileName : BasicObj.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import pygame


class Plane(object):

    def __init__(self, type, speed, pos, blood, window, imgPath):
        self._type = type
        self._speed = speed
        self._pos = pos
        self._blood = blood
        self._window = window
        self._imgPath = imgPath
        self._imgPlane = pygame.image.load(self._imgPath)
        self.update()

    def update(self):
        self._window.window().blit(self._imgPlane, [self._pos[0] - self._imgPlane.get_width() / 2,
                                                    self._pos[1] - self._imgPlane.get_height() / 2])

    def speed(self):
        return self._speed

    def position(self):
        return self._pos

    def height(self):
        return self._imgPlane.get_height()

    def width(self):
        return self._imgPlane.get_width()

    def type(self):
        return self._type

    def blood(self):
        return self._blood

    def bloodOp(self, value):
        self._blood += value

    def move(self, direction, speed, passable):  # passable: is able to fly out of screen or not
        if (self._pos[0] + direction[0] * speed >= 0
                and self._pos[0] + direction[0] * speed - self.height() / 2 <= self._window.width()):
            self._pos[0] += direction[0] * speed
        if (passable or self._pos[1] + direction[1] * speed >= 0 + self.width() / 2
                and self._pos[1] + direction[1] * speed - self.height() / 2 <= self._window.height()):
            self._pos[1] += direction[1] * speed

    def erasable(self):
        if self._pos[1] - self.height() / 2 > self._window.height():
            return True
        elif self._blood <= 0:
            return True
        else:
            return False


# logically, bullets are also a type of plane
class Bullet(Plane):

    def __init__(self, Owner, window, type, speed, blood, imgPath):
        self._owner = Owner
        # print(Owner.head())
        super(Bullet, self).__init__(type, speed, Owner.head(), blood, window, imgPath)

    def fly(self, direction):
        self.move(direction, self._speed, True)


def collide(plane1, plane2):
    r1 = (plane1.height() + plane2.width()) / 8
    r2 = (plane2.height() + plane2.width()) / 8
    powDistance = pow(plane1.position()[0] - plane2.position()[0], 2.0) + \
                  pow(plane1.position()[1] - plane2.position()[1], 2.0)
    return powDistance < pow(r1 + r2, 2.0)
