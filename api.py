from board import Board
import pygame
import sys


class Api:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        board = self.board.make_board()
        new_board = ""
        for line in board:
            new_board += "".join(line) + "\n"
        return new_board

    def game_is_running(self):
        return not self.board.checkmate

    def play(self, coords):
        if not coords:
            return
        try:
            coords = [int(coords[0]), int(coords[1])]
        except ValueError:
            return (self.get_board(), "solo se permiten numeros")
        except IndexError:
            return(self.get_board(), "")
        move_array = self.board.play(coords[0], coords[1])
        move_array = "" if not move_array else move_array
        if type(move_array) is bool:
            move_array = "jaque" if move_array else move_array
        move_array = "promover? si:(10 4): " if move_array == "promotion" else(
            move_array)
        return (self.get_board(), move_array)

    def get_coords(self, s, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                coords = [int((event.pos[0]) / 50), int((event.pos[1]) / 50)]
                return coords

    def draw_screen(self, screen, settings):
        screen.fill(settings.background_color)
        white, black, board, movearray, sign = (
            self.board.get_pygame_objects(screen, settings))
        for element in board:
            element.draw()
        for piece in white:
            piece.draw()
        for piece in black:
            piece.draw()
        try:
            for element in movearray:
                element.draw()
        except TypeError:
            pass
        if sign:
            sign.draw()
        pygame.display.flip()
