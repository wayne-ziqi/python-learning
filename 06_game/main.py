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
import Bullet

global mainScene
global mainClock
global Hero
global Enemies


def gameInit():
    pygame.init()  # 导入并初始化pygame的包
    global mainScene
    mainScene = MainWindow(480, 700)
    mainScene.windowUpdate()
    # set the plane's moving window and position
    global Hero
    Hero = Plane.PlaneHero(1, [mainScene.width() / 2, mainScene.height() - 100], mainScene)

    global Enemies
    Enemies = Plane.EnemyList()

    global HeroBullets
    HeroBullets = Bullet.BulletList(Hero, mainScene)

    pygame.display.update()
    global mainClock
    mainClock = pygame.time.Clock()


def eventProc():
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            gameQuit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            Hero.fly(event.pos)

def gameQuit():
    pygame.quit()


if __name__ == '__main__':
    # game initializing
    gameInit()
    time.sleep(3)
    global mainScene
    global mainClock
    global Hero
    global Enemies
    # game main loop
    while True:
        # set game frame rate: 60s is appropriate

        mainClock.tick(120)
        # check user's interaction

        eventProc()
        Hero.fire()
        # Hero.move([-1,-1])
        Enemies.Enemy_generate(mainScene)
        Enemies.Enemy_exec()

        # update images
        Hero.Hero_update()
        Enemies.update()

        pygame.display.update()
        # update screen
        mainScene.windowUpdate()

        # listen to the end event
