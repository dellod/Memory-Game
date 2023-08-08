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
        self.curr_guess = 1
        self.circles = {}


    def level_up(self) -> int:
        self.curr_max += 1
        return self.curr_max


    def level_down(self) -> int:
        if self.curr_max > 1:
            self.curr_max -= 1
        return self.curr_max


    def increment_guess(self) -> int:
        self.curr_guess += 1
        return self.curr_guess


    def reset_guess(self) -> int:
        self.curr_guess = 1
        return self.curr_guess


    def randomize_circles(self, display) -> None:
        self.circles.clear()
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
            for key, circle in self.circles.items():
                if circle.check_if_collide_with_circle(position, constants.CIRCLE_RAD):
                    do_restart = True
                    break
            if do_restart:
                continue

            self.circles[i] = (number_circle.NumberCircle(display, position, i))
            i += 1


    def hide_all_circles(self) -> None:
        for key, circle in self.circles.items():
            circle.hide_circle()


    def unhide_all_circles(self) -> None:
        for key, circle in self.circles.items():
            circle.unhide_circle()


    def unhide_all_circles_only_if_hidden(self) -> None:
        for key, circle in self.circles.items():
            if circle.status == number_circle.CircleStatus.HIDDEN:
                circle.unhide_circle()


    def draw_circles(self) -> None:
        for key, circle in self.circles.items():
            circle.draw_circle()()


    def check_circle_touched(self):
        for key, circle in self.circles.items():
            if circle.detect_circle_click(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                return [key, circle]

        return [-1, None]
