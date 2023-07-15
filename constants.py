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
BLACK           = (0, 0, 0)
WHITE           = (255, 255, 255)
RED             = (180, 0, 0)
NICE_BLUE       = (37, 150, 190)
NICE_GREEN      = (35, 173, 72)

# Fonts
pygame.init()
NUMBER_FONT = pygame.font.Font('freesansbold.ttf', 32)

# Game Background
GAME_BACKGROUND_PATH = ".\\public\\images\\game_background.jpg"
BACKGROUND_POS = (0,0)
BACKGROUND_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# SCORE
CURRENT_SCORE_POSITION = (75, 25)

# Number Circle
CIRCLE_RAD = 50

# Events
def QUIT_FUNC():
    global RUNNING
    RUNNING = False
QUIT_EVENT = event.Event("QUIT", QUIT_FUNC, predefined=pygame.QUIT)


EVENTS = [QUIT_EVENT]