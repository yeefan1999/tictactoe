`"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    
    xcount = 0
    ocount = 0
    
    for row in board:
        xcount += row.count(X)
        ocount += row.count(O)
        
    if xcount == ocount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY :
                moves.append([i,j])
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print('Spot already occupied')
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xcount = 0
    ocount = 0
    #horizontal check
    for row in board:
        xcount = row.count(X)
        ocount = row.count(O)
        
        if xcount == 3:
            return X
        if ocount == 3:
            return O
        
    #vertical check
    for i in range(0,3):
        if (board[0][i] != EMPTY and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]
    
    #diagonal check
    if (board[0][0]!=EMPTY and
        board[0][0] == board[1][1] and
        board[1][1] == board[2][2] ):
        return board[0][0]
    
    if (board[0][2]!=EMPTY and
        board[0][2] == board[1][1] and
        board[1][1] == board[2][0] ):
        return board[0][2]
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptycount = 0
    for row in board:
        emptycount += row.count(EMPTY)
    
    if emptycount == 0:
        return True
    
    if winner(board) is not None:
        return True
    
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:

        max_value = -math.inf
        moves = actions(board)
        
        for move in moves:
            maxx = min_(result(board,move))
            if maxx > max_value:
                max_value = maxx
                decision = move
            
    else:

        min_value = math.inf
        moves = actions(board)
        for move in moves:
            minn = max_(result(board,move))
            if minn < min_value:
                min_value = minn
                decision = move
    
    return decision

    raise NotImplementedError
    
def max_(board):
    
    if terminal(board):
        return utility(board)
    
    max_value = -math.inf
    moves = actions(board)
    for move in moves:
        maxx = min_(result(board,move))
        if maxx > max_value:
            max_value = maxx
            
    return max_value
    
    raise NotImplementedError


def min_(board):
    
    if terminal(board):
        return utility(board)
    
    min_value = math.inf
    moves = actions(board)
    for move in moves:
        minn = max_(result(board,move))
        if minn < min_value:
            min_value = minn
            action = move
            
    return min_value
    
    raise NotImplementedError
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

