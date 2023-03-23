"""
Authors: Christian Shepperson & Samantha Noggle
An implementation of the 
game hounds and hare.
The game plays using the minimax
algorithm for both players.
"""
import abc

"""
builds the edges of the board
"""
EDGES = {
    0: {1, 2, 3},
    1: {0, 2, 4, 5},
    2: {0, 1, 3, 5},
    3: {0, 2, 5, 6},
    4: {1, 5, 7},
    5: {1, 2, 3, 4, 6, 7, 8, 9},
    6: {3, 5, 9},
    7: {4, 5, 8, 10},
    8: {5, 7, 9, 10},
    9: {5, 6, 8, 10},
    10: {7, 8, 9},
}

class HoundsAndHareError(AttributeError):
    """
    This class is used to indicate a problem in the H & H game.
    """

class HoundsAndHare:
    """
    This class implements Hounds and Hares.
    The board is represented as a two-dimensional list.  Each
    location on the board contains one of the following symbols:
       'h1' for Hound 1
       'h2' for hound 2
       'h3' for hound 3
       'A' for the Hare
       '_' for an empty location
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
        self.board[0] = "h1"
        self.board[1] = "h2"
        self.board[3] = "h3"


    def __str__(self):
        return self.boardToStr(self.board)


        
    def boardToStr(self, board):
        """
        Returns a string representation of the konane board.
        """
        result = "  "
        for i in range(self.size):
            result += str(i) + " "
        result += "\n"
        for i in range(self.size):
            result += str(i) + " "
            for j in range(self.size):
                result += str(board[i][j]) + " "
            result += "\n"
        return result

    def can_move(self, player, current_pos, new_pos):
        if self.board[new_pos] != "_":
            return False
        if current_pos == new_pos:
            return False
        if player.turn == 'hounds':
            if current_pos - new_pos > 1 or current_pos == 10 or new_pos == 0:
                return False
            if new_pos in EDGES[current_pos]:
                return True
            else:
                return False
        else:
            # hare
            if new_pos in EDGES[current_pos]:
                return True
            else:
                return False

    def valid(self, row):
        """
        Returns true if the given row and col represent a valid location on
        the H & H board.
        """
        return row >= 0 and row <= 10

    def get_hare_position(self):
        """
        returns the current position of the hare
        """
        for key, val in self.board.items():
            if val == "A":
                return key

    def get_hounds_position(self):
        h1 = -1
        h2 = -1
        h3 = -1
        for key, val in self.board.items():
            if val == "h1":
                h1 = key
            elif val == "h2":
                h2 = key
            elif val == "h3":
                h3 = key
        return (h1, h2, h3)
    

    def contains(self, board, row, symbol):
        """
        Returns true if the given row and col represent a valid location on
        the H & H board and that lcoation contains the given symbol.
        """
        return self.valid(row) and board[row]==symbol

    def makeMove(self, player, move):
        """
        Updates the current board with the next board created by the given
        move.
        """
        self.board = self.nextBoard(self.board, player, move)

    def nextBoard(self, board, player, move):
        """
        Given a move for a particular player from (r1,c1) to (r2,c2) this
        executes the move on a copy of the current H & H board.  It will
        raise a HoundsAndHareError if the move is invalid. It returns the copy of
        the board, and does not change the given board.
        """
    def generateHoundMoves(self):
        """
        Generates all legal moves for the three Hounds
        """
        moves_hound1 = []
        moves_hound2 = []
        moves_hound3 = []
        pos_hound1, pos_hound2, pos_hound3 = self.get_hounds_position()
        possible_moves_hound1 = EDGES[pos_hound1]
        possible_moves_hound2 = EDGES[pos_hound2]
        possible_moves_hound3 = EDGES[pos_hound3]
        for move_pos in possible_moves_hound1:
            if self.can_move('hounds', current_pos=pos_hound1, new_pos=move_pos):
                    moves_hound1.append(move_pos)
        for move_pos in possible_moves_hound2:
            if self.can_move('hounds', current_pos=pos_hound2, new_pos=move_pos):
                    moves_hound2.append(move_pos)
        for move_pos in possible_moves_hound3:
            if self.can_move('hounds', current_pos=pos_hound3, new_pos=move_pos):
                    moves_hound3.append(move_pos)
        return (moves_hound1, moves_hound2, moves_hound3)

    def generateHareMoves(self):
        """
        Generates all legal moves for the Hare
        """
        moves = []
        pos = self.get_hare_position()
        possible_moves = EDGES[pos]
        for move_pos in possible_moves:
            if self.can_move('hare', current_pos=pos, new_pos=move_pos):
                moves.append(move_pos)
        return moves

    def generateMoves(self, board, player):
        """
        Generates and returns all legal moves for the given player using the
        current board configuration.
        """

        if player.turn == "Hare":
            return self.generateHareMoves()
        else:
            return self.generateHoundMoves()


    def switch_turn(self): 
        if self.turn == "A":
            self.turn = "O" 
        
        else:  self.turn = "A"
    
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
    name = "Player"
    wins = 0
    losses = 0
    def results(self):
        result = self.name
        result += " Wins:" + str(self.wins)
        result += " Losses:" + str(self.losses)
        result += " Score: " + str(self.score())
        return result

    def score(self):
        return self.wins - self.losses

    def lost(self):
        self.losses += 1

    def won(self):
        self.wins += 1
    def reset(self):
        self.wins = 0
        self.losses = 0

    @abc.abstractmethod
    def initialize(self, side):
        """
        Records the player's side, either 'O' for hound or
        'A' for Hare.  Should also set the name of the player.
        """


    @abc.abstractmethod
    def getMove(self, board):
        """
        Given the current board, should return a valid move.
        """
        return

class HumanPlayer(Player):
    """
    Prompts a human player for a move.
    """
    def initialize(self, side):
        self.side = side
        self.name = "Human"

    def getMove(self, board):
        if self.side == "A":
            inputs = list(map( int, input("Enter a valid move for Hare: ").split()))
        else:
            inputs = list(map( int, input("Enter which hare to move and a valid move: ").split()))
        if inputs[1] == -1:
            return []
        return inputs

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
