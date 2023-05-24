# !/usr/bin/env python3
# @file block.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import constants


####################################################################################################
# BLOCK CLASS
####################################################################################################
class NumberCircle:
    def __init__(self, surface: pygame.surface, position: tuple, number: int) -> None:
        self.surface = surface
        self.position = position
        self.number = number

        self.circle = None

    def draw_circle_with_number(self) -> None:
       # Draw Cirle
       self.circle = pygame.draw.circle(
                            self.surface,
                            constants.NICE_BLUE,
                            self.position,
                            constants.CIRCLE_RAD,
                            width=10
                                       )

       # Draw number
       num = constants.NUMBER_FONT.render(
           str(self.number),
           True,
           constants.BLACK
                                         )
       num_rect = num.get_rect()
       num_rect.center = self.position

       # Blit
       self.surface.blit(num, num_rect)