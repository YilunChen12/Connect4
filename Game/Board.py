import numpy as np


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board_elements = np.zeros((self.rows, self.cols))

    def flip_board(self):
        return np.flip(self.board_elements, 0)
