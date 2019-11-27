import pygame.font
import pygame


class Piece():
    def __init__(self, screen, settings, letter, x, y, color):
        self.color = color
        self.text_color = self.prep_color(color)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.prep_rect(color, settings, letter, x, y)
        self.x = (settings.block_size/2) + x * settings.block_size
        self.y = (settings.block_size/2) + y * settings.block_size
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def prep_color(self, color):
        if color == "white":
            return (250, 250, 250)
        elif color == "black":
            return (0, 0, 0)
        elif color == "movearray":
            return (250, 0, 250)
        elif color == "board":
            return (240, 180, 60)

    def draw(self):
        if self.color == "movearray" or self.color == "board":
            pygame.draw.rect(self.screen, self.text_color, self.rect)
        elif self.color == "black" or self.color == "white":
            self.screen.blit(self.image, self.rect)

    def prep_rect(self, color, settings, letter, x, y):
        if color == "movearray":
            self.image = pygame.Rect(x, y, settings.move_array_block_size,
                                     settings.move_array_block_size)
            self.rect = pygame.Rect(x, y, settings.move_array_block_size,
                                    settings.move_array_block_size)
        elif color == "black" or color == "white":
            self.font = pygame.font.SysFont(None, settings.piece_font_size)
            self.image = self.font.render(letter, True, self.text_color)
            self.rect = self.image.get_rect()
        elif color == "board":
            self.image = pygame.Rect(x, y, settings.block_size - 5,
                                     settings.block_size - 5)
            self.rect = pygame.Rect(x, y, settings.block_size-5,
                                    settings.block_size - 5)
