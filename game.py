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
import memory_logic
import pygame
import score
from enum import Enum


####################################################################################################
# GAME STATUS
####################################################################################################
class GameStatus(Enum):
    MENU                = 0
    LEVEL_ANNOUNCEMENT  = 1
    ROUND_START         = 2
    ROUND_GUESS         = 3
    GUESSED_CORRECTLY   = 4
    GUESSED_INCORRECTLY = 5


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

        # Setup current score
        self.current_score = score.Score()

        # Setup memory logic component
        self.logic = memory_logic.MemoryLogic()

        # Declare status of game
        self.status = GameStatus.MENU


    def set_clock_tick(self, FPS) -> None:
        self.clock.tick(FPS)


    def update_display(self) -> None:
        pygame.display.update()


    def close(self) -> None:
        pygame.quit()


    def load_image(self, filepath: str, is_alpha_convert: bool, scale_size: tuple) -> pygame.surface.Surface:
        if is_alpha_convert:
            img = pygame.image.load(filepath).convert_alpha()
        else:
            img = pygame.image.load(filepath).convert()

        img = pygame.transform.scale(img, scale_size)
        return img


    def start_round(self):
        self.logic.randomize_circles(display=self.display)
        self.logic.unhide_all_circles()
        self.logic.draw_circles()
        self.update_display()
        pygame.time.wait(1500)
        self.logic.hide_all_circles()
        self.status = GameStatus.ROUND_GUESS


    def start_guess(self):
        self.logic.draw_circles()
        user_guess = self.logic.check_circle_touched()
        if user_guess[0] != -1:
            if user_guess[0] == self.logic.curr_guess:
                user_guess[1].guess_correct()
                self.logic.increment_guess()
                if self.check_if_level_up():
                    self.setup_next_round_level_up()
            elif user_guess[0] > self.logic.curr_guess:
                user_guess[1].guess_incorrect()
                self.setup_next_round_level_down()


    def check_if_level_up(self) -> bool:
        if self.logic.curr_guess > self.logic.curr_max:
            return True
        else:
            return False


    def setup_next_round_level_up(self) -> None:
        self.logic.level_up()
        self.logic.reset_guess()
        self.status = GameStatus.ROUND_START


    def setup_next_round_level_down(self) -> None:
        self.logic.level_down()
        self.logic.reset_guess()
        self.status = GameStatus.ROUND_START


    def check_and_run_status(self):
        SWITCH = {
            GameStatus.MENU: self.run_menu,
            GameStatus.LEVEL_ANNOUNCEMENT: self.announce_level,
            GameStatus.ROUND_START: self.start_round,
            GameStatus.ROUND_GUESS: self.start_guess,
        }
        return SWITCH[self.status]


    def run_menu(self) -> None:
        pass


    def announce_level(self) -> None:
        pass


    def run_game(self) -> None:
        # TODO: remove later, skipping menu and going right into round start just for testing
        self.status = GameStatus.ROUND_START
        # Load images
        bg = self.load_image(constants.GAME_BACKGROUND_PATH, False, constants.BACKGROUND_SIZE)

        # Run game loop
        while constants.RUNNING:
            # Use event checker to check events
            self.event_checker.check_events()

            # Set tick rate for clock
            self.set_clock_tick(constants.FPS)

            # Blit background
            self.display.blit(bg, constants.BACKGROUND_POS)

            # Show score
            self.current_score.update_score(self.logic.curr_max)
            self.current_score.draw_curr_score(self.display)

            # check and run status
            self.check_and_run_status()()

            # Update pygame display
            self.update_display()

        self.close()
