# !/usr/bin/env python3
# @file block.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import constants
import math


####################################################################################################
# BLOCK CLASS
####################################################################################################
class NumberCircle:
    def __init__(self, surface: pygame.surface, position: tuple, number: int) -> None:
        self.surface = surface
        self.position = position
        self.number = number

        self.circle = None
        self.hidden = True

    def draw_circle_with_number(self) -> None:
       # Draw Circle
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

       # Blit text
       self.surface.blit(num, num_rect)

       # Change hidden flag to False
       self.hidden = False


    def draw_circle_with_number_hidden(self) -> None:
       # Draw Circle
        self.circle = pygame.draw.circle(
                            self.surface,
                            constants.NICE_BLUE,
                            self.position,
                            constants.CIRCLE_RAD
                                       )

        # Change hidden flag to False
        self.hidden = True


    def draw_circle_with_guess_correct(self) -> None:
        # Draw Circle
       self.circle = pygame.draw.circle(
                            self.surface,
                            constants.NICE_GREEN,
                            self.position,
                            constants.CIRCLE_RAD,
                                       )

       # Draw number
       num = constants.NUMBER_FONT.render(
           str(self.number),
           True,
           constants.BLACK
                                         )
       num_rect = num.get_rect()
       num_rect.center = self.position

       # Blit text
       self.surface.blit(num, num_rect)

       # Change hidden flag to False
       self.hidden = False


    def draw_circle_with_guess_incorrect(self) -> None:
        # Draw Circle
       self.circle = pygame.draw.circle(
                            self.surface,
                            constants.RED,
                            self.position,
                            constants.CIRCLE_RAD,
                                       )

       # Draw number
       num = constants.NUMBER_FONT.render(
           str(self.number),
           True,
           constants.BLACK
                                         )
       num_rect = num.get_rect()
       num_rect.center = self.position

       # Blit text
       self.surface.blit(num, num_rect)

       # Change hidden flag to False
       self.hidden = False


    def detect_circle_click(self, pos, clicked_tuple) -> bool:
        # Check if position collides with the circle and it has been clicked
        return self.circle.collidepoint(pos) and clicked_tuple[0]


    def check_if_collide_with_circle(self, c2_pos, c2_rad) -> bool:
        # Pythagorean theorem
        distance = math.sqrt((math.pow(c2_pos[0] - self.position[0], 2))
                             + (math.pow(c2_pos[1] - self.position[1], 2)))

        # Check if distance is less than 2 circle radius
        if distance < (constants.CIRCLE_RAD * 2):
            return True
        else:
            return False
