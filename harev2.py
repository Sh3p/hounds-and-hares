"""
Authors: Christian Shepperson & Samantha Noggle
An implementation of the 
game hounds and hare.
"""
import abc
import random
import traceback
import copy

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
        self.turn = '0'
        self.reset()

    def reset(self):
        """
        Resets the starting board state.
        """
        self.board = ['_'] * 11
        self.board[10] = 'A'
        self.board[0] = 'h1'
        self.board[1] = 'h2'
        self.board[3] = 'h3'


    def __str__(self):
        return self.boardToStr(self.board)


    def boardToStr(self, board):
        """
        Returns a string representation of the H & H board.

        board array is laid out like:
        X 1 4 7 X
        0 2 5 8 10
        X 3 6 9 X
        """
        topRow = f"X {board[1]} {board[4]} {board[7]} X"
        midRow = f"\n{board[0]} {board[2]} {board[5]} {board[8]} {board[10]}"
        botRow = f"\nX {board[3]} {board[6]} {board[9]} X"

        return f"{topRow}{midRow}{botRow}"

    def can_move(self, board , player, current_pos, new_pos):
        """
        Checks if a move is valid given a current position and new position
        Checks which side player is on
        
        """
        if not self.valid(new_pos):
            return False
        if board[new_pos] != '_':
            return False
        if current_pos == new_pos:
            return False
        if player == 'O':
            if current_pos - new_pos > 1 or current_pos == 10 or new_pos == 0:
                return False
            if new_pos in EDGES[current_pos]:
                return True
            else:
                return False
        if player == 'A':
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

    def get_hare_position(self, board):
        """
        returns the current position of the hare
        """
        hare = board.index('A')
        return hare

    def get_hounds_position(self, board):
        """
        returns the current position of the hounds
        """
        h1 = board.index('h1')
        h2 = board.index('h2')
        h3 = board.index('h3')
      
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
        Given a move for a particular player 'A' for hare, h1 for hound 1, 
        h2 for hound 2, h3 for hound 3, this
        executes the move on a copy of the current H & H board.  It will
        raise a HoundsAndHareError if the move is invalid. It returns the copy of
        the board, and does not change the given board.
        """

        temp = copy.deepcopy(board)

        startPos = move[0] 
        endPos =  move[1] 

        if player == 'A':
            if self.can_move(board, 'A' , startPos, endPos):
                hare_val = temp[startPos]
                temp[startPos] = '_'
                temp[endPos] = hare_val
                self.switch_turn()
                return temp
            else: return print("move invalid")
        else: 
            if self.can_move(board,'O', startPos, endPos):
                hound_val = temp[startPos]
                temp[startPos] = '_'
                temp[endPos] = hound_val
                self.switch_turn()
                return temp
            else: return print("move invalid")

    def generateHoundMoves(self, board):
        """
        Generates all legal moves for the three Hounds
        """
        moves_hound1 = []
        moves_hound2 = []
        moves_hound3 = []
        pos_hound1, pos_hound2, pos_hound3 = self.get_hounds_position(board)
        possible_moves_hound1 = EDGES[pos_hound1]
        possible_moves_hound2 = EDGES[pos_hound2]
        possible_moves_hound3 = EDGES[pos_hound3]
        for move_pos in possible_moves_hound1:
            if self.can_move(board,'O' , current_pos=pos_hound1, new_pos=move_pos):
                    move_list1 = []
                    move_list1.append(pos_hound1)
                    move_list1.append(move_pos)
                    moves_hound1.append(move_list1)
        for move_pos in possible_moves_hound2:
            if self.can_move(board, 'O' , current_pos=pos_hound2, new_pos=move_pos):
                    move_list2 = []
                    move_list2.append(pos_hound2)
                    move_list2.append(move_pos)
                    moves_hound2.append(move_list2)
        for move_pos in possible_moves_hound3:
            if self.can_move(board ,'O', current_pos=pos_hound3, new_pos=move_pos):
                    move_list3 = []
                    move_list3.append(pos_hound3)
                    move_list3.append(move_pos)
                    moves_hound3.append(move_list3)
        total_moves = moves_hound1 + moves_hound2 + moves_hound3
        return total_moves

    def generateHareMoves(self, board):
        """
        Generates all legal moves for the Hare
        """
        moves = []
        pos = self.get_hare_position(board)
        possible_moves = EDGES[pos]
        for move_pos in possible_moves:
            if self.can_move(board, 'A', pos, move_pos):
                move_list1 = []
                move_list1.append(pos)
                move_list1.append(move_pos)
                moves.append(move_list1)
        return moves

    def generateMoves(self, board, player):
        """
        Generates and returns all legal moves for the given player using the
        current board configuration.
        """

        if player == 'A':
            return self.generateHareMoves(board)
        else:
            return self.generateHoundMoves(board)

    def switch_turn(self): 
        if self.turn == 'A':
            self.turn = 'A' 
        
        else:  self.turn = 'A'
    
    def is_game_over(self, board):
        """
        Returns true if the hare has reached the 
        leftmost position, or has passed the leftmost hound
        """
        if board[0] == 'A':
            return True
        if "_" not in self.board:
            return True

        hounds_pos = [i for i, x in enumerate(board) if x == "H"]

        hare_pos = board.index('A')

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
        self.reset()
        p1.initialize('O')
        p2.initialize('A')
        print (p1.name, "vs", p2.name)
        while 1:
            if self.is_game_over(self.board):
                return 'A'
            if show:
                print ("Player Hounds's turn")
            try:
                move = p1.getMove(self.board)
            except Exception as e:
                print ("player Hound is forfeiting because of error:", str(e))
                print(traceback.format_exc())

                move = []
            if move == []:
                result = 'A'
                break
            try:
                self.makeMove('O', move)
            except HoundsAndHareError:
                print ("ERROR: invalid move by", p1.name)
                print(traceback.format_exc())
                result = 'A'
                break
            if self.is_game_over(self.board):
                return 'O'
            if show:
                print (move)
                print
                print(self)
                print ("player Hare's turn")
            try:
                move = p2.getMove(self.board)
            except Exception as e:
                print ("player Hare is forfeiting because of error:", str(e))
                print(traceback.format_exc())

                move = []
            if move == []:
                result = 'O'
                break
            try:
                self.makeMove('A', move)
            except HoundsAndHareError:
                print ("ERROR: invalid move by", p2.name)
                print(traceback.format_exc())
                result = 'O'
                break
            if show:
                print (move)
                print(self)
                print
            
        if show:
            print ("Game over")
        return result
    
    def playNGames(self, n, p1, p2, show):
        """
        Will play out n games between player p1 and player p2.
        The players alternate going first.  Prints the total
        number of games won by each player.
        """
        first = p1
        second = p2
        for i in range(n):
            print ("Game", i + 1)
            winner = self.playOneGame(first, second, show)
            if winner == 'B':
                first.won()
                second.lost()
                print (first.name, "wins")
            else:
                first.lost()
                second.won()
                print (second.name, "wins")
            temp = first
            first = second
            second = temp




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
    def getMove(self):
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

    def getMove(self):
        if self.side == "A":
            inputs = list(map( int, input("Enter a valid move for Hare: ").split()))
        else:
            inputs = list(map( int, input("Enter which hound to move and a valid move: ").split()))
        if inputs[1] == -1:
            return []
        return inputs

class RandomPlayer(HoundsAndHare, Player):
    """
    Chooses a random move from the set of possible moves.
    """
    def initialize(self, side):
        self.side = side
        self.name = "RandomPlayer"

    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        if n == 0:
            return []
        else:
            return moves[random.randrange(0, n )]


class SimplePlayer(HoundsAndHare, Player):
    """
    Always chooses the first move from the set of possible moves.
    """
    def initialize(self, side):
        self.side = side
        self.name = "SimplePlayer"


    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        
        if n == 0:
            return []
        else:
            return moves[0]

class MinimaxPlayer(HoundsAndHare, Player):
    """
    Uses minimax to determine moves
    """
    def __init__(self, depthLimit):
        HoundsAndHare.__init__(self)
        self.limit = depthLimit

    def initialize(self, side):
        self.side = side
        self.name = "MinimaxPlayer"


    def max(self, board, depth):
        moves = self.generateMoves(board, self.side)
        bestMove = 0
        currentMove = -float("inf")

        if depth > self.depthLimit:
            return self.eval(board)

        for move in moves:
            bestVal = (self.min(self.nextBoard(board, self.side, move), depth+1))
            if bestVal > currentMove:
                currentMove = bestVal
                bestMove = move

        return currentMove, bestMove

    def min(self, board, depth):
        moves = self.generateMoves(board, self.side)
        bestMove = 0
        currentMove = float("inf")

        if depth > self.depthLimit:
            return self.eval(board)

        for move in moves:
            bestVal = (self.max(self.nextBoard(board, self.side, move), depth+1))
            if bestVal > currentMove:
                currentMove = bestVal
                bestMove = move

        return currentMove, bestMove  
                

    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        if not moves:
            return []

        value = []
        alpha = -float("inf")
        for move in moves:
            value.append(self.minimax(self.nextBoard(board, self.side, move), 1, alpha, float("inf")))
            if max(value) > alpha:
                alpha = max(value)
        return moves[value.index(max(value))]

    def minimax(self, board, depth, alpha, beta):
        if depth >= self.limit:
            return self.eval(board)
        isMax = depth % 2 == 0
        if isMax:
            next_boards = self.helper(board, self.side)
        else:
            next_boards = self.helper(board, self.switch_turn())

        if not next_boards:
            if isMax:
                return -float("inf")
            else:
                return float("inf")
        value = []
        new_alpha = alpha
        new_beta = beta
        for next_board in next_boards:
            if value:
                if isMax:
                    if max(value) >= beta:
                        break
                    if max(value) > alpha:
                        new_alpha = max(value)
                else:
                    if min(value) <= alpha:
                        break
                    if min(value) < beta:
                        new_beta = min(value)

            value.append(self.minimax(next_board, depth+1, new_alpha, new_beta))

        if isMax:
            return max(value)
        else:
            return min(value)

    def helper(self, board, side):
        moves = self.generateMoves(board, side)
        boards = []
        for move in moves:
            boards.append(self.nextBoard(board, side, move))
        return boards

    def eval(self, board):
        return len(self.generateMoves(board, self.side))


game = HoundsAndHare()
game.playNGames(2,RandomPlayer(), RandomPlayer(), 1)
