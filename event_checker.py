# !/usr/bin/env python3
# @file event_checker.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import event

####################################################################################################
# EVENT CHECKER CLASS
####################################################################################################
class EventChecker:
    def __init__(self, events: list[event.Event]) -> None:
        self.events = events

    def check_events(self) -> None:
        for event in pygame.event.get():
            for e in self.events:
                if event.type == e.id:
                    e.action()

