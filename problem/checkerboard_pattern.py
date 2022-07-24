import numpy as np


def print_check_board(n):
    print("Checkerboard pattern:")
    x = np.zeros((n, n), dtype=int)
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()


n = 8
print_check_board(n)
