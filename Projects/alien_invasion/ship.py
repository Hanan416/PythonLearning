import pygame
from settings import Settings
import os


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()
        self.load_image()

    def load_image(self):
        """Load the default ship image or a specific one choosen by the user."""
        self.image = pygame.image.load(os.getcwd() + self.settings.ships_path + self.settings.default_ship)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)