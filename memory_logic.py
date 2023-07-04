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
    def __init__(self, curr_max: int = 1) -> None:
        self.curr_max = curr_max
        self.curr_correct = 0 # how much the user has guessed correct
        self.wrong_guess_num = -1
        self.circles = {}


    def level_up(self) -> int:
        self.curr_max += 1
        self.curr_correct = 0
        return self.curr_max


    def level_down(self) -> int:
        if self.curr_max > 1:
            self.curr_max -= 1
        self.curr_correct = 0
        return self.curr_max


    def increment_curr_correct(self) -> None:
        self.curr_correct += 1


    def compare_guess_and_curr(self, guess: int) -> bool:
        if guess == self.curr_max:
            return True
        else:
            return False


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
            for key, circle in self.circles.items():
                if circle.check_if_collide_with_circle(position, constants.CIRCLE_RAD):
                    do_restart = True
                    break
            if do_restart:
                continue

            self.circles[i] = (number_circle.NumberCircle(display, position, i))
            i += 1


    def draw_circles(self) -> None:
        for key, circle in self.circles.items():
            if key <= self.curr_correct:
                circle.draw_circle_with_guess_correct()
            elif key == self.wrong_guess_num:
                circle.draw_circle_with_guess_incorrect()
            else:
                circle.draw_circle_with_number_hidden()

    def check_circle_touched(self) -> int:
        for key, circle in self.circles.items():
            if circle.detect_circle_click(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                return key

        return -1


    def check_levelup(self) -> bool:
        if self.curr_max == self.curr_correct:
            return True
        else:
            return False