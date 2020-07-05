#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Minzhang Li
# FILE: C:\Users\Administrator\Desktop\python数据分析\python基础语法以及配套练习(持续更新)-lmz\basic\day3\game.py
# DATE: 2020/07/05 Sun
# TIME: 19:38:35

# DESCRIPTION: This is a main game file for alien-invasion

import pygame as pg
import math
from ship import Ship 
from setting import Setting

def run_game():
    pg.init()
    setting = Setting()
    screen = pg.display.set_mode(
        (setting.screen_width, setting.screen_height)
    )
    player = Ship(screen)
    pg.display.set_caption("Alien Invasion")

    while True:
        screen.fill(setting.bg_color)
        player.blitme()
        pg.display.flip()


if __name__ == '__main__':
    run_game()