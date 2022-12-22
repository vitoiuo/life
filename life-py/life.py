# ## Todo: melhorar inputs
# # An example code to take matrix input by user  
  
# Rows = int(input("Give the number of rows:"))  
# Columns = int(input("Give the number of columns:"))  
  
# # Initializing the matrix  
# example_matrix = []  
  
# # taking RowsxColumns matrix from the user  
# for i in range(Rows):  
#     # taking input for the row from the user  
#     single_row = list(map(int, input().split()))  
#     # appending the 'single_row' to the 'example_matrix'  
#     example_matrix.append(single_row)  
# # printing the matrix given by user  
# print(example_matrix)  

import copy
import time

import numpy as np


def init_day_of_life ():

    #User entry
    rows = int(input("Give the number of rows:"))  
    columns = int(input("Give the number of columns:"))

    matrix = []
    for i in range(rows):
        single_row = list(map(int, input().split()))
        if (len(single_row) > columns):
            raise Exception("Não ultrapasse o limite de colunas determinado!")
        matrix.append(single_row)  

    #Life game
    board = np.array(matrix)
    while(np.any(board == 1)):
        print(board)
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


init_day_of_life()