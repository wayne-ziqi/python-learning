#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/23 21:53
# @Author   : Wayne Qi
# @FileName : PushButton.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import pygame


class PushButton(object):
    def __init__(self, window, pos, path1, path2=None):
        self._image1 = pygame.image.load(path1)
        if path2:
            self._image2 = pygame.image.load(path2)
        else:
            self._image2 = None
        self._height = self._image1.get_height()
        self._width = self._image1.get_width()
        self._window = window
        self._pos = pos
        self._curImage = self._image1

    def height(self):
        return self._height
    def width(self):
        return self._width
    def catch(self, pos):
        return self._pos[0] <= pos[0] <= self._pos[0] + self._width \
               and self._pos[1] <= pos[1] <= self._pos[1] + self._height

    def press(self):
        if self._image2:
            self._curImage = self._image2
        else:
            self._curImage = self._image1

    def release(self):
        self._curImage = self._image1

    def update(self):
        self._window._window.blit(self._curImage, self._pos)
