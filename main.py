from Game.Board import Board
from Game.Player import Player
from Game.AiPlayer import AiPlayer
from Game.connect4 import Connect4
import Game.Constants as CONS
import sys
import pygame
import math
import random


class Game:
    def __init__(self):
        self.board = Board(CONS.ROW_COUNT, CONS.COL_COUNT)
        self.player = Player(CONS.RED)
        self.ai_player = AiPlayer(CONS.YELLOW)
        self.connect4 = Connect4(self.board, self.player, self.ai_player)

        self.game_over = False

    # handle end game
    def game_stop(self):
        pass


if __name__ == '__main__':
    game = Game()
    while not game.game_over:
        game.connect4.game_loop()
        # ask for player 1 input

        # ask for player 2 input


