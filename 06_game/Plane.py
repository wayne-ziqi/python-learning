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
        imgPlane = pygame.image.load(imgPath)
        self._window.blit(imgPlane, (pos[0] - imgPlane.get_width() / 2, pos[1] - imgPlane.get_height() / 2))
        pygame.display.update()

    def position(self):
        return self._pos

    def move(self, direction):
        self._pos[0] += direction[0]
        self._pos[1] += direction[1]


class PlaneHero(Plane):
    def __init__(self, pos, window):
        super(PlaneHero, self).__init__('Hero', pos, window, 'images/me1.png')


