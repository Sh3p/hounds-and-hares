# A possible solution to the lab with 
# different heursitics

from harev2 import *

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

    def distanceBetween(self, board, p1, p2):
        """
        Gets the distance between two pieces

        :param board: The board
        :param p1: String of a piece (h1, h2, A)
        :param p2: String of a piece (h1, h2, A)
        :return: The taxicab distance between p1 and p2
                (not the amount of moves it is away)
        """
        p1Loc = [self.getRow(board, p1), self.getColumn(board, p1)]
        p2Loc = [self.getRow(board, p2), self.getColumn(board, p2)]

        return sum(abs(val1-val2) for val1, val2 in zip(p1Loc, p2Loc))



    def eval(self, board):
        #      ----- Generalized Heursistics -----

        # How many possible next does this move give the player
        moves = len(self.generateMoves(board, self.side))
    
        # How many more moves than the player's opponent
        moreMoves = (len(self.generateMoves(board, self.side))) - (len(self.generateMoves(board, self.opponent)))

        #      -----      Hare Specific      -----

        # Distance from goal spot
        goalDist = self.getColumn(board, 'A')

        # Cumulative manhattan distance from Hounds

        # How many hounds are to the right of the hare


        # How far away is the move from the closest hound 

        #      -----     Hound Specific      -----

        # Proximity to eachother

        # Cumulative Distance from Hare



        return moreMoves

game = HoundsAndHare()
game.playNGames(100, MinimaxPlayer(5), RandomPlayer(), False)