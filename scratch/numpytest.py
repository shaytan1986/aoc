import numpy as np
from pprint import pprint as pp
a = np.array([[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]])
pp(a)
pp(a[:, 2])
# # Third col: [ 2  6 10 14]
# print(a[1, :])
# # Second row: [4 5 6 7]
# print(a[1, ::2])
# # Second row, every other element: [4 6]
# print(a[:, :-1])
# # All columns except last:
# # [[ 0  1  2]
# # [ 4  5  6]
# # [ 8  9 10]
# # [12 13 14]]
# print(a[:-2])
# # Same as a[:-2, :]
# # [[ 0  1  2  3]
# # [ 4  5  6  7]]
