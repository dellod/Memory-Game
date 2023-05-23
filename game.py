# !/usr/bin/env python3
# @file game.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import constants
import event
import event_checker
import pygame


####################################################################################################
# GAME CLASS
####################################################################################################
class Game:
    """
    Class that represents the instance of the game.

    Attributes
    ----------
        display (pygame.Surface): The display the game will be drawn to.
        clock (pygame.time.Clock)
        running (boolean)
    """

    def __init__(self) -> None:
        """
        Init function
        """
        # Init PyGame
        pygame.init()

        # Init display
        self.display = pygame.display.set_mode((constants.SCREEN_SIZE))
        pygame.display.set_caption(constants.GAME_CAPTION)

        # Set-up clock
        self.clock = pygame.time.Clock()

        # Create Event Checker object
        self.event_checker = event_checker.EventChecker(constants.EVENTS)

    def close(self) -> None:
        pygame.quit()

    def run_game(self) -> None:
        while constants.RUNNING:
            # Use event checker to check events
            self.event_checker.check_events()
        self.close()
