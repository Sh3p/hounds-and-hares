"""
Authors: Christian Shepperson & Samantha Noggle
An implementation of the 
game hounds and hare.
The game plays using the minimax
algorithm for both players.
"""
import abc

class HoundsAndHareError(AttributeError):
    """
    This class is used to indicate a problem in the H & H game.
    """

class HoundsAndHare:
    """
    This class implements Hounds and Hares.
    The board is represented as a two-dimensional list.  Each
    location on the board contains one of the following symbols:
       'O' for a Hound
       'A' for the Hare
       '.' for an empty location
    The hounds always go first. Hounds may move vertically or 
    horizontally, but never left. The Hare may move in any direction.
    The Hounds win if they can corner the Hare so that it has no 
    empty adjacent spots. The Hare wins if it reaches the leftmost 
    tile, or passes the leftmost Hound. Also, if the Hounds move 
    sideways (vertically) 10 turns in a row, it is "stalling" and the 
    Hare automatically wins.
    """

    def __init__(self):
        self.turn = "O"
        self.reset()

    def reset(self):
        """
        Resets the starting board state.
        """
        self.board = ["_"] * 11
        self.board[10] = "A"
        self.board[0] = "O"
        self.board[1] = "O"
        self.board[3] = "O"


    def __str__(self):
        pass

    def boardToStr(self, board):
        """
        Returns a string representation of the H & H board.
        """
        pass

    def valid(self, row, col):
        """
        Returns true if the given row and col represent a valid location on
        the H & H board.
        """
        pass

    def contains(self, board, row, col, symbol):
        """
        Returns true if the given row and col represent a valid location on
        the H & H board and that lcoation contains the given symbol.
        """
        pass

    def makeMove(self, player, move):
        """
        Updates the current board with the next board created by the given
        move.
        """
        pass

    def nextBoard(self, board, player, move):
        """
        Given a move for a particular player from (r1,c1) to (r2,c2) this
        executes the move on a copy of the current H & H board.  It will
        raise a HoundsAndHareError if the move is invalid. It returns the copy of
        the board, and does not change the given board.
        """
    def generateHoundMoves(board):
        """
        Generates all legal moves for the three Hounds
        """
        pass

    def generateHareMoves(board):
        """
        Generates all legal moves for the Hare
        """
        pass

    def generateMoves(self, board, player):
        """
        Generates and returns all legal moves for the given player using the
        current board configuration.
        """

        # use the previous two methods
        pass

    def switch_turn(self):
        self.turn = "H" if self.turn == "Hare" else "Hare"
    
    def is_game_over(self):
        """
        Returns true if the hare has reached the 
        leftmost position, or has passed the leftmost hound
        """
        if "_" not in self.board:
            return True

        hounds_pos = [i for i, x in enumerate(self.board) if x == "H"]

        hare_pos = self.board.index("Hare")

        for h in hounds_pos:
            if abs(hare_pos - h) == 10:
                return True

        return False
    
    def playOneGame(self, p1, p2, show):
        """
        Given two instances of players, will play out a game
        between them.  Returns 'O' if the Hounds win, or 'A' if
        the Hare wins. When show is true, it will display each move
        in the game.
        """
        pass
    
    def playNGames(self, n, p1, p2, show):
        """
        Will play out n games between player p1 and player p2.
        Prints the total number of games won by each player.
        """




class Player(metaclass = abc.ABCMeta):
    """
    A base class for H & H players.  All players must implement
    the the initialize and getMove methods.
    """
    pass

class HumanPlayer(Player):
    """
    Prompts a human player for a move.
    """

class RandomPlayer(HoundsAndHare, Player):
    """
    Chooses a random move from the set of possible moves.
    """

class SimplePlayer(HoundsAndHare, Player):
    """
    Always chooses the first move from the set of possible moves.
    """




    # Code for the AI player

    # def minimax(self, depth, is_maximizing):
    #     if depth == 0 or self.is_game_over():
    #         return 0

    #     if is_maximizing:
    #         max_value = -1
    #         for i, cell in enumerate(self.board):
    #             if cell == "_":
    #                 self.board[i] = self.turn
    #                 value = self.minimax(depth - 1, False)
    #                 self.board[i] = "_"
    #                 max_value = max(max_value, value)
    #         return max_value
    #     else:
    #         min_value = 1
    #         for i, cell in enumerate(self.board):
    #             if cell == "_":
    #                 self.board[i] = self.turn
    #                 value = self.minimax(depth - 1, True)
    #                 self.board[i] = "_"
    #                 min_value = min(min_value, value)
    #         return min_value
    # #determines the best move of possible moves from minimax
    # def best_move(self):
    #     max_value = -1
    #     best_move = None
    #     for i, cell in enumerate(self.board):
    #         if cell == "_":
    #             self.board[i] = self.turn
    #             value = self.minimax(9, False)
    #             self.board[i] = "_"
    #             if value > max_value:
    #                 max_value = value
    #                 best_move = i
    #     return best_move


# #exceutes a game
# def play_game():
#     game = HoundsAndHare()
#     while not game.is_game_over():
#         print("Current Board:", " ".join(game.board))
#         move = game.best_move()
#         print("Best move:", move)
#         game.board[move] = game.turn
#         game.switch_turn()
#         print("Final Board:", " ".join(game.board))


# play_game()
