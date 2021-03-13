import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import colors

'''mock-up of grid visualization'''


def board_visual_solution(N, solution_matrix_index):  # function to convert solution matrix into a chess board
    board = np.zeros((N, N))  # blank board
    for i in solution_matrix_index:
        board[math.floor(i / N), i % N] += 1  # coordinates found
        # by rounding down x= index divided by N , and y=index modulo N
    colour_map = colors.ListedColormap(['yellow', 'green'])
    plt.figure(figsize=(N, N))
    plt.pcolor(board[::-1], cmap=colour_map, edgecolors='k', linewidths=3)
    plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    return plt.show()


index = [1, 7, 8, 14]  # the index of the rows in the sample solution after other rows eliminated
board_visual_solution(4, index)

index = [3, 14, 18, 31, 33, 44, 48, 61]  # 8*8 chessboard sample
board_visual_solution(8, index)
