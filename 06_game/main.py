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

from PushButton import PushButton
from MainWindow import MainWindow
import Plane
import Bullet
import BasicObj
from SubWindow import BeginWindow

global beginScene
global mainScene
global mainClock
global Hero
global Enemies
global endButton
global resButton


def eventProcBegin():
    global beginScene
    eventList = pygame.event.get()
    beginCaught = False
    for event in eventList:
        if event.type == pygame.QUIT:
            gameQuit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and beginScene._btnBegin.catch(event.pos):
            beginCaught = True
            beginScene._btnBegin.press()
            return -1
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = 0
            if beginScene._btnBegin.catch(event.pos):
                flag = 1
            else:
                flag = 0
            beginScene._btnBegin.release()
            return flag


# def eventProcEnd(endButton, resButton):
#     eventList = pygame.event.get()
#     endCaught = False
#     againCaught = False
#     for event in eventList:
#         if event.type == pygame.QUIT:
#             gameQuit()
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if endButton.catch(event.pos):
#                 endCaught = True
#             elif resButton.catch(event.pos):
#                 againCaught = True
#
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if endCaught:
#                 if endButton.catch(event.pos):
#                     gameQuit()
#                     exit()
#             elif againCaught:
#                 if resButton.catch(event.pos):
#                     flag = 1
#                 else:
#                     flag = 0
#                 return flag


def gameHello():
    pygame.init()  # 导入并初始化pygame的包
    global beginScene
    beginScene = BeginWindow(480, 700)
    beginScene.windowUpdate()
    global mainClock
    mainClock = pygame.time.Clock()
    beginScene.windowUpdate()
    end = False

    while True:
        mainClock.tick(120)
        start = eventProcBegin()
        if start == 1:
            end = gameStart()
        if end:
            pass
        pygame.display.update()
        beginScene.windowUpdate()


def gameInit():
    # pygame.init()
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
    # global mainClock
    # mainClock = pygame.time.Clock()


def gameStart():
    # game initializing
    gameInit()
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
        Plane.killEnemy(Hero, Enemies)
        # Hero.move([-1,-1])
        Enemies.Enemy_generate(mainScene)
        Enemies.Enemy_exec()

        # update images
        Hero.Hero_update()
        Enemies.update()

        pygame.display.update()
        # update screen
        mainScene.windowUpdate()
        end = gameEnd()
        if end: return end

        # listen to the end event


def gameEnd():
    global Hero
    global Enemies
    t1 = Plane.killHero(Hero, Enemies)
    return t1


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
    gameHello()
