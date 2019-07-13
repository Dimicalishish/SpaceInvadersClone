import pygame


class SpaceInvaders:
    def __init__(self, settings):
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.size)


class Settings:
    def __init__(self, size):
            self.size = size


if __name__ == "__main__":
    game_settings = Settings((800, 600))
    game = SpaceInvaders(game_settings)
