#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:03
# @Author   : Wayne Qi
# @FileName : Plane.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

'game main file'

import pygame
import time
from MainWindow import MainWindow
import Plane


global mainScene
global mainClock
global Hero

def gameInit():
    pygame.init()#导入并初始化pygame的包
    global mainScene
    mainScene = MainWindow(480, 700)

    #set the plane's moving window and position
    global Hero
    Hero = Plane.PlaneHero([mainScene.width()/2, mainScene.height() - 100], mainScene)
    mainScene.windowUpdate()
    global mainClock
    mainClock = pygame.time.Clock()

def gameQuit():
    pygame.quit()


if __name__ == '__main__':
    # game initializing
    gameInit()
    time.sleep(3)
    global mainScene
    global mainClock
    global Hero
    #game main loop
    while True:
        # set game frame rate: 60s is appropriate

        mainClock.tick(60)
        # check user's interaction

        Hero.move([-1,-1])
        # update images
        Hero.update()
        # update screen
        mainScene.windowUpdate()

        #listen to the end event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
                exit()



