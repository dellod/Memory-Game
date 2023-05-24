# !/usr/bin/env python3
# @file constants.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import event
import pygame

####################################################################################################
# CONSTANTS
####################################################################################################
# Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Game Caption
GAME_CAPTION = "Memory Game by Daryl Dang"

# Clock Speed
FPS = 60

# Running
RUNNING = True

# Colours
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)

# Key Positions
BACKGROUND_POS = (0,0)

# Key Sizes
BACKGROUND_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# File Paths
GAME_BACKGROUND_PATH = ".\\public\\images\\game_background.jpg"

# Events
def QUIT_FUNC():
    global RUNNING
    RUNNING = False
QUIT_EVENT = event.Event("QUIT", QUIT_FUNC, predefined=pygame.QUIT)


EVENTS = [QUIT_EVENT]