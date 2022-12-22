import copy

import numpy as np


def init_day_of_life (matrix):
    board = np.array(matrix)
    
    print(board)
    for ridx, row in enumerate(board):
        for cidx, _ in enumerate(row):
            cel_value = board[ridx, cidx]
            test_board = copy.deepcopy(board)
            test_board[ridx, cidx] = 0

            row_range = [ridx-1,ridx+2] if ridx != 0 else [ridx,ridx+2]
            col_range = [cidx-1,cidx+2] if cidx != 0 else [cidx,cidx+2]
            
            neighbourhood = test_board[row_range[0]:row_range[1], col_range[0]:col_range[1]]
            print(np.count_nonzero(neighbourhood))
            # board[0:2, 0:3]


init_day_of_life([[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0,], [0, 0, 0, 0]])