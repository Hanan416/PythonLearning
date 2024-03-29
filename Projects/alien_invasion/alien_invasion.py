import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class dedicated for managing the game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.init_display()

        self.ship = Ship(self)

    def run_game(self):
        """Game main loop."""
        while True:
            self.handle_input_events()
            self.handle_display()

    def handle_display(self):
        # Redraw the screen
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def handle_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def init_display(self):
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_length))
        pygame.display.set_caption(self.settings.caption)
        self.bg_color = self.settings.bg_color


if __name__ == '__main__':
    # Create game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
