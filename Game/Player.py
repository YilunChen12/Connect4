class Player:
    def __init__(self, color):
        self.color = color

    def select(self):
        selection = int(input("Player 1 make your choice: "))
        return selection
