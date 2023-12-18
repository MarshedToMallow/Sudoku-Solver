from board import Board

import numpy as np

if __name__ == "__main__":
    table = np.array([
        [0, 9, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 6, 0, 0, 8, 7, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 7],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [4, 0, 8, 0, 0, 1, 6, 0, 0],
        [0, 2, 0, 0, 0, 0, 4, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 0, 0],
        [9, 0, 4, 8, 0, 0, 0, 0, 5]
    ])

    board = Board.from_table(table)
    board.search()