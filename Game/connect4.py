import Game.Constants as CONS


class Connect4:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
        self.col_selection = None

    def drop_piece(self, row, col, piece):
        self.board.board_elements[row][col] = piece

    def is_valid_location(self):
        col = self.col_selection
        return self.board.board_elements[5][col] == 0

    def get_next_open_rows(self):
        col = self.col_selection
        for r in range(CONS.ROW_COUNT):
            if self.board.board_elements[r][col] == 0:
                return r

    def player1_selection(self):
        # ask for player 1 selection
        player1_selection = self.player1.select()
        self.col_selection = player1_selection
        return self.col_selection

    def player2_selection(self):
        # ask for player 2 selection
        player2_selection = self.player2.select()
        self.col_selection = player2_selection
        return self.col_selection

    def game_loop(self):
        if self.turn == 0:
            print(self.player1_selection())
            if self.is_valid_location():
                row = self.get_next_open_rows()
                col = self.col_selection
                self.drop_piece(row, col, 1)
        else:
            print(self.player2_selection())
            if self.is_valid_location():
                row = self.get_next_open_rows()
                col = self.col_selection
                self.drop_piece(row, col, 2)

        print(self.board.flip_board())
        self.turn += 1
        self.turn = self.turn % 2
