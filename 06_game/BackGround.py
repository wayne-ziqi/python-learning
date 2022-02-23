#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/23 19:26
# @Author   : Wayne Qi
# @FileName : BackGround.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import pygame

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
