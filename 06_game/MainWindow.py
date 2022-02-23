#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:27
# @Author   : Wayne Qi
# @FileName : MainWindow.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

"class main window, user's playground"
import pygame

class MainWindow(object):
    def __init__(self, width = 0, height = 0):
        self._window = pygame.display.set_mode((width, height))
        # self._bkImg = pygame.image.load("images/background.png")
        # self.windowUpdate()
        self.backGround = BackGround(self)

    def windowUpdate(self):
        self.backGround.update()
        #pygame.display.update()

    def width(self):
        return self._window.get_width()
    def height(self):
        return self._window.get_height()
    def window(self):
        return self._window


class BackGround(object):

    def __init__(self, window):
        self._image1 = pygame.image.load("images/background.png")
        self._image2 = pygame.image.load("images/background.png")
        self._h1 = -window.height()
        self._h2 = 0
        self._height = window.height()
        self._click = 0
        self._delay = 5
        self._window = window

    def scroll(self):
        self._h1 += 1
        self._h2 += 1
        if self._h1 == self._height:
            self._h1 = -self._height
        if self._h2 == self._height:
            self._h2 = -self._height

    def scrollable(self):
        self._click +=1
        if self._click >= self._delay:
            self._click = 0
            return True
        return False

    def update(self):
        if self.scrollable():
            self.scroll()
        self._window._window.blit(self._image1,(0,self._h1))
        self._window._window.blit(self._image2, (0, self._h2))
