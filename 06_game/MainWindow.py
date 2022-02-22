#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:27
# @Author   : Wayne Qi
# @FileName : MainWindow.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

import pygame

class MainWindow(object):
    def __init__(self, width = 0, height = 0):
        self._window = pygame.display.set_mode((width, height))
        self._bkImg = pygame.image.load("images/background.png")
        self.windowUpdate()

    def windowUpdate(self):
        self._window.blit(self._bkImg,(0,0))
        #pygame.display.update()

    def width(self):
        return self._window.get_width()
    def height(self):
        return self._window.get_height()
    def window(self):
        return self._window