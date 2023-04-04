class AiPlayer:
    def __init__(self, color):
        self.color = color

    def select(self):
        selection = int(input("Player 2 make your choice: "))
        return selection
