#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/22 9:03
# @Author   : Wayne Qi
# @FileName : Plane.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

"""all planes defined here"""
import random

import pygame


class Plane(object):

    def __init__(self, type, speed, pos, blood, window, imgPath):
        self._type = type
        self._speed = speed
        self._pos = pos
        self._blood = blood
        self._window = window
        self._imgPath = imgPath
        self._imgPlane = pygame.image.load(self._imgPath)
        self.update()

    def update(self):
        self._window.window().blit(self._imgPlane, [self._pos[0] - self._imgPlane.get_width() / 2,
                                                    self._pos[1] - self._imgPlane.get_height() / 2])

    def speed(self):
        return self._speed

    def position(self):
        return self._pos

    def height(self):
        return self._imgPlane.get_height()

    def width(self):
        return self._imgPlane.get_width()

    def move(self, direction, speed, passable):  # passable: is able to fly out of screen or not
        if (self._pos[0] + direction[0] * speed >= 0 + self.height() / 2
                and self._pos[0] + direction[0] * speed - self.height() / 2 <= self._window.width()):
            self._pos[0] += direction[0] * speed
        if (passable or self._pos[1] + direction[1] * speed >= 0 + self.width() / 2
                and self._pos[1] + direction[1] * speed - self.height() / 2 <= self._window.height()):
            self._pos[1] += direction[1] * speed

    def erasable(self):
        if self._pos[1] - self.height() / 2 > self._window.height():
            return True
        elif self._blood == 0:
            return True
        else:
            return False


class PlaneHero(Plane):
    def __init__(self, speed, pos, window):
        super(PlaneHero, self).__init__('Hero', speed, pos, 1, window, 'images/me1.png')
        self._head = [self.position()[0], self.position()[1] - self.height() / 2]

    def head(self):
        return self._head

    def catch(self, pos):
        return self._pos[0] + self.width() / 2 >= pos[0] >= self._pos[0] - self.width() / 2 \
               and self._pos[1] + self.height() / 2 >= pos[1] >= self._pos[1] - self.height() / 2

    def fly(self, pos):
        if self.catch(pos):
            self.move([pos[0] - self.position()[0], pos[1] - self.position()[1]], self.speed(), False)


class PlaneEnemy1(Plane):
    def __init__(self, speed, pos, window):
        super(PlaneEnemy1, self).__init__('Enemy1', speed, pos, 5, window, 'images/enemy1.png')
        self._head = [self.position()[0], self.position()[1] + self.height() / 2]

    def head(self):
        return self._head

    def exec(self):
        self.move([0, 2], self._speed, True)


class PlaneEnemy2(Plane):
    def __init__(self, speed, pos, window):
        super(PlaneEnemy2, self).__init__('Enemy2', speed, pos, 10, window, 'images/enemy2.png')
        self._head = [self.position()[0], self.position()[1] + self.height() / 2]

    def head(self):
        return self._head

    def exec(self):
        self.move([0, 1.5], self._speed, True)


class PlaneEnemy3(Plane):
    def __init__(self, speed, pos, window):
        super(PlaneEnemy3, self).__init__('Enemy3', speed, pos, 20, window, 'images/enemy3_n1.png')
        self._head = [self.position()[0], self.position()[1] + self.height() / 2]

    def exec(self):
        self.move([0, 1], self._speed, True)


class EnemyList(object):
    def __init__(self):
        self._list = []
        self._tick = 0
        self._delay = 30
        self._clockStart = 0

        self._minEnemyNum = 5
        self._maxEnemyNum = 10

    def __len__(self):
        return len(self._list)

    def add_enemy(self, type_enemy, speed, position, window):
        if type_enemy == 1:
            position[1] -= PlaneEnemy1(0, [-1000, -1000], window).height() / 2
            self._list.append(PlaneEnemy1(speed, position, window))
        elif type_enemy == 2:
            position[1] -= PlaneEnemy2(0, [-1000, -1000], window).height() / 2
            self._list.append(PlaneEnemy2(speed, position, window))
        elif type_enemy == 3:
            position[1] -= PlaneEnemy3(0, [-1000, -1000], window).height() / 2
            self._list.append(PlaneEnemy3(speed, position, window))

    def update(self):
        for i in range(len(self._list) - 1, -1, -1):
            if self._list[i] and self._list[i].erasable():
                del self._list[i]
        for i in range(len(self._list)):
            self._list[i].update()

    def enemy_addable(self):
        self._tick += 1

        if self._tick >= self._delay:
            self._tick = 0
            self._delay = random.randint(50, 200)
            return True
        else:
            return False

    def Enemy_generate(self, mainScene):

        if self.enemy_addable() and len(self._list) < self._maxEnemyNum:
            randType = random.randint(1, 3)
            randSpeed = random.uniform(0.5, 1)
            randPos = [random.randint(0, mainScene.width()), 0]
            self.add_enemy(randType, randSpeed, randPos, mainScene)

    def Enemy_exec(self):
        for enemy in self._list:
            enemy.exec()
