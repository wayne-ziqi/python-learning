#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:03
# @Author   : Wayne Qi
# @FileName : Plane.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import pygame


class Plane(object):

    def __init__(self, type, pos, window, imgPath):
        self._type = type
        self._pos = pos
        self._window = window
        self._imgPath = imgPath
        self._imgPlane = pygame.image.load(self._imgPath)
        self.update()

    def update(self):
        self._window.window().blit(self._imgPlane, [self._pos[0] - self._imgPlane.get_width() / 2,
                                                    self._pos[1] - self._imgPlane.get_height() / 2])
        pygame.display.update()

    def position(self):
        return self._pos

    def height(self):
        return self._imgPlane.get_height()

    def wight(self):
        return self._imgPlane.get_width()

    def move(self, direction):
        if (self._pos[0] + direction[0] >= 0 + self.height() / 2
                and self._pos[0] + direction[0] - self.height() / 2 <= self._window.width()):
            self._pos[0] += direction[0]
        if (self._pos[1] + direction[1] >= 0 + self.wight() / 2
                and self._pos[1] + direction[1] - self.height() / 2 <= self._window.height()):
            self._pos[1] += direction[1]


class PlaneHero(Plane):
    def __init__(self, pos, window):
        super(PlaneHero, self).__init__('Hero', pos, window, 'images/me1.png')
