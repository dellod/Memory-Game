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
import number_circle
import pygame
import time # TODO: remove later

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

        # Set level
        self.level = 1


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


    def clear_board(self):
        pass


    def show_correct_screen(self):
        # this will display a screen that shows that the guess was correct
        # TODO: remove below
        print("correct guess")
        time.sleep(2)

    def show_wrong_screen(self):
        # this will display a screen that shows that the guess was wrong
        # TODO: remove below
        print("WRONG guess")
        time.sleep(2)


    def run_game(self) -> None:
        # Load images
        bg = self.load_image(constants.GAME_BACKGROUND_PATH, False, constants.BACKGROUND_SIZE)

        # Setup memory logic component
        logic = memory_logic.MemoryLogic(self.level) # Pass in init level
        logic.randomize_circles(display=self.display)

        # Run game loop
        while constants.RUNNING:
            # Use event checker to check events
            self.event_checker.check_events()

            # Set tick rate for clock
            self.set_clock_tick(constants.FPS)

            # Blit background
            self.display.blit(bg, constants.BACKGROUND_POS)

            # Draw circles in memory
            logic.draw_circles()

            # Check which circle was pressed
            user_guess = logic.check_circle_touched()
            if user_guess != -1:
                if logic.compare_guess_and_curr(user_guess):
                    self.show_correct_screen()
                    logic.increment_curr_correct()
                else:
                    logic.wrong_guess_num = user_guess
                    self.show_wrong_screen()
                    logic.level_down()
                    logic.randomize_circles(display=self.display)

            # Check if we can level up
            if logic.check_levelup():
                logic.level_up()
                logic.randomize_circles(display=self.display)

            # Draw circles in memory
            logic.draw_circles()

            # Update pygame display
            self.update_display()

        self.close()
