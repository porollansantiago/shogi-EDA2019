from api import Api
from settings import Settings
import pygame

if __name__ == "__main__":
    api_shogi = Api()
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    while True:
        coord = api_shogi.get_coords(s, screen)
        api_shogi.play(coord)
        api_shogi.draw_screen(screen, s)
