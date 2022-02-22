#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:03
# @Author   : Wayne Qi
# @FileName : Plane.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

'game main file'

import pygame as game

def gameInit():
    game.init()#导入并初始化pygame的包

def gameQuit():
    game.quit()

if __name__ == '__main__':
    gameInit()
    gameQuit()