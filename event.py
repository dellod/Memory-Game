# !/usr/bin/env python3
# @file event.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import pygame


####################################################################################################
# EVENT CLASS
####################################################################################################
class Event:
    def __init__(self, event_name: str, action, predefined=None) -> None:
        self.name = event_name
        self.action = action

        if predefined is None:
            self.id = pygame.USEREVENT + 1
        else:
            self.id = predefined

    def set_timer_event(self, ms: int):
        pygame.time.set_timer(self.id, ms)
