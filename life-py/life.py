import copy

import numpy as np


def init_day_of_life (matrix):
    board = np.array(matrix)
    while(np.any(board == 1)):
        print(board)
        test_board = copy.deepcopy(board)
        for ridx, row in enumerate(board):
            for cidx, _ in enumerate(row):
                cel_value = board[ridx, cidx]

                row_range = [ridx-1,ridx+2] if ridx != 0 else [ridx,ridx+2]
                col_range = [cidx-1,cidx+2] if cidx != 0 else [cidx,cidx+2]
                
                neighbourhood = board[row_range[0]:row_range[1], col_range[0]:col_range[1]]
                neighbours_number= np.count_nonzero(neighbourhood)

                if(cel_value):
                    match neighbours_number-1:
                        case 0 | 1:
                            test_board[ridx, cidx] = 0
                        case 2 | 3:
                            test_board[ridx, cidx] = 1
                        case other:
                            test_board[ridx, cidx] = 0
                elif(neighbours_number == 3):
                    test_board[ridx, cidx] = 1
        board = test_board


init_day_of_life([ 
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
     ])