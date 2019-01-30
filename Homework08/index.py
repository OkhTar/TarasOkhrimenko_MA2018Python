"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    
    while board.check_win() == None:
        empty_list = board.get_empty_squares()
        next_operation = empty_list[random.randrange(len(empty_list))]
        board.move(next_operation[0], next_operation[1], player)
        player = provided.switch_player(player)
        
def mc_update_scores(scores, board, player):

    if board.check_win() == None or board.check_win() == provided.DRAW:
        return
    
    if board.check_win() == player:
        match_score = SCORE_CURRENT
        other_score = -1 * SCORE_OTHER
    else:
        match_score = -1 * SCORE_CURRENT
        other_score = SCORE_OTHER
    
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            status = board.square(row, col)
            if status == provided.EMPTY:
                pass
            elif status == player:
                scores[row][col] += match_score
            else:
                scores[row][col] += other_score
