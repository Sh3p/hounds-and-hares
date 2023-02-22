"""
Author: Christian Shepperson
An implementation of the 
game hounds and hare.
The game plays using the minimax
algorithm for both players.
"""

class HoundsAndHare:
    #sets up game state
    def __init__(self):
        self.board = ["_"] * 9
        self.board[0] = "Hare"
        self.turn = "H"
    
    def switch_turn(self):
        self.turn = "H" if self.turn == "Hare" else "Hare"
    #determines if game ends
    def is_game_over(self):
        if "_" not in self.board:
            return True
        
        hounds_pos = [i for i, x in enumerate(self.board) if x == "H"]

        hare_pos = self.board.index("Hare")
        
        for h in hounds_pos:
            if abs(hare_pos - h) == 10:
                return True
        
        return False
    #algorithm used to determine moves
    def minimax(self, depth, is_maximizing):
        if depth == 0 or self.is_game_over():
            return 0
        
        if is_maximizing:
            max_value = -1
            for i, cell in enumerate(self.board):
                if cell == "_":
                    self.board[i] = self.turn
                    value = self.minimax(depth - 1, False)
                    self.board[i] = "_"
                    max_value = max(max_value, value)
            return max_value
        else:
            min_value = 1
            for i, cell in enumerate(self.board):
                if cell == "_":
                    self.board[i] = self.turn
                    value = self.minimax(depth - 1, True)
                    self.board[i] = "_"
                    min_value = min(min_value, value)
            return min_value
    #determines the best move of possible moves from minimax
    def best_move(self):
        max_value = -1
        best_move = None
        for i, cell in enumerate(self.board):
            if cell == "_":
                self.board[i] = self.turn
                value = self.minimax(9, False)
                self.board[i] = "_"
                if value > max_value:
                    max_value = value
                    best_move = i
        return best_move


#exceutes a game
def play_game():
    game = HoundsAndHare()
    while not game.is_game_over():
        print("Current Board:", " ".join(game.board))
        move = game.best_move()
        print("Best move:", move)
        game.board[move] = game.turn
        game.switch_turn()
        print("Final Board:", " ".join(game.board))


play_game()
