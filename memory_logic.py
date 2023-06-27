# !/usr/bin/env python3
# @file memory_logic.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import pygame
import constants
import number_circle
import random


####################################################################################################
# MEMORY CLASS
####################################################################################################
class MemoryLogic:
    def __init__(self) -> None:
        self.curr_max = 1
        self.circles = []


    def level_up(self) -> int:
        self.curr_max += 1
        return self.curr_max


    def level_down(self) -> int:
        if self.curr_max > 1:
            self.curr_max -= 1
        return self.curr_max

    def randomize_circles(self, display) -> None:
        i = 1
        while i <= self.curr_max:
            do_restart = False
            position = (random.uniform(0 + constants.CIRCLE_RAD,
                                       constants.SCREEN_SIZE[0] - constants.CIRCLE_RAD
                                      ),
                        random.uniform(0 + constants.CIRCLE_RAD,
                                       constants.SCREEN_SIZE[1] - constants.CIRCLE_RAD,
                                      )
                       )
            for circle in self.circles:
                if circle.check_if_collide_with_circle(position, constants.CIRCLE_RAD):
                    do_restart = True
                    break
            if do_restart:
                continue

            self.circles.append(number_circle.NumberCircle(display, position, i))
            i += 1


    def draw_circles(self) -> None:
        for circle in self.circles:
            circle.draw_circle_with_guess_correct()
