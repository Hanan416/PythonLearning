class Settings:
    """A class to store all the game settings."""

    def __init__(self):
        """Initialize the game settings."""
        self.init_screen_settings()
        self.init_resources()

    def init_screen_settings(self):
        self.screen_width = 1280
        self.screen_length = 720
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invasion"

    def init_resources(self):
        self.resource_path = '\\resources'
        self.art_path = self.resource_path + '\\art'
        self.ships_path = self.art_path + '\\ships'
        self.default_ship = '\\xenis-blue-a-1.png'
