import pygame.font
import pygame
from pygame.sprite import Group

class Piece():
    def __init__(self, screen, settings, letter, x, y, color):
        self.color = color
        self.text_color = self.prep_color(color)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = self.prep_rect(color, settings, letter, x, y)
        self.rect = self.image.get_rect()
        self.x = x * settings.block_size
        self.y = x * settings.block_size
        self.rect.left = self.screen_rect.left + self.x
        self.rect.top = self.screen_rect.top + self.y

    def prep_color(self, color):
        if color == "white":
            return (250, 250, 250)
        elif color == "black":
            return (0, 0, 0)
        elif color == "movearray":
            return (250, 0, 250)

    def show_score(self):
        if self.color == "movearray":
            pygame.draw.rect(self.screen, self.text_color, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def prep_rect(self, color, settings, letter, x, y):
        if color == "movearray":
            return pygame.Rect(x, y, 25, 25)
        else:
            self.font = pygame.font.SysFont(None, settings.piece_font_size)
            return self.font.render(letter, True, self.text_color)