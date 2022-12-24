import copy
import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def init_day_of_life ():

    rows = int(input("Give the number of rows:"))  
    columns = int(input("Give the number of columns:"))

    matrix = []
    for i in range(rows):
        single_row = list(map(int, input().split()))
        if (len(single_row) > columns):
            raise ValueError("Não ultrapasse o limite de colunas determinado!")
        matrix.append(single_row)  

    board = np.array(matrix)

    colors = ['black', 'white']
    bounds = [0,1]
    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    plt.imshow(board, interpolation='none', cmap=cmap, norm=norm)
    plt.grid()
    plt.show()

    while(np.any(board == 1)):
        time.sleep(1)

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
        
        plt.imshow(board, interpolation='none', cmap=cmap, norm=norm)
        plt.grid()
        plt.show()
        next = str(input('Continuar? (Yes or No)'))
        if(next == 'No'):
            break


init_day_of_life()