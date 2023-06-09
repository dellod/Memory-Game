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


    def run_game(self) -> None:
        # Load images
        bg = self.load_image(constants.GAME_BACKGROUND_PATH, False, constants.BACKGROUND_SIZE)

        # Setup memory logic component
        test = memory_logic.MemoryLogic()
        test.curr_max = 10
        test.randomize_circles(display=self.display)

        # Run game loop
        while constants.RUNNING:
            # Use event checker to check events
            self.event_checker.check_events()

            # Set tick rate for clock
            self.set_clock_tick(constants.FPS)

            # Blit background
            self.display.blit(bg, constants.BACKGROUND_POS)

            # TODO: testing, remove later
            test.draw_circles()
            print(test.check_circle_touched())

            # Update pygame display
            self.update_display()

        self.close()
