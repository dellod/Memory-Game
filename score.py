# !/usr/bin/env python3
# @file block.py
# Memory Game
# Daryl Dang

####################################################################################################
# IMPORTS
####################################################################################################
import constants
import pygame


####################################################################################################
# SCORE CLASS
####################################################################################################
class Score:
    # TODO: this class will also be responsible for keeping score later
    def __init__(self, score: int=1) -> None:
        self.curr_score = score


    def update_score(self, new_score: int) -> None:
        self.curr_score = new_score


    def draw_curr_score(self, surface) -> None:
        score = constants.NUMBER_FONT.render(
            "Guess: " + str(self.curr_score),
            True,
            constants.BLACK
                                            )
        score_rect = score.get_rect()
        score_rect.center = constants.CURRENT_SCORE_POSITION

        # Blit text
        surface.blit(score, score_rect)