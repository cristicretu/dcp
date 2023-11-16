"""
16.11.2023

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
"""

import time
import random

class Solution:
    def find_min_max_from_matrix_naive(self, matrix, point1, point2):
        rows = len(matrix)
        
        if rows < 1:
            raise ValueError("Row must be bigger at least 1")

        cols = len(matrix[0]) 

        if cols < 1:
            raise ValueError("Cols must be bigger at least 1")

        x1, y1 = point1
        x2, y2 = point2

        if x1 < 0 or x1 > rows or y1 < 0 or y2 > cols:
            raise ValueError("point1 is out of bounds")

        if x2 < 0 or x2 > rows or y2 < 0 or y2 > cols:
            raise ValueError("point2 is out of bounds")

        small_number = matrix[x1][y1]
        big_number = matrix[x2][y2]

        res = sum(value < small_number or value > big_number for row in matrix for value in row)

        return res

    def find_min_max_from_matrix(self, matrix, point1, point2):
        rows = len(matrix)
        
        if rows < 1:
            raise ValueError("Row must be bigger at least 1")

        cols = len(matrix[0]) 

        if cols < 1:
            raise ValueError("Cols must be bigger at least 1")

        x1, y1 = point1
        x2, y2 = point2

        if x1 < 0 or x1 > rows or y1 < 0 or y2 > cols:
            raise ValueError("point1 is out of bounds")

        if x2 < 0 or x2 > rows or y2 < 0 or y2 > cols:
            raise ValueError("point2 is out of bounds")

        small_number = matrix[x1][y1]
        big_number = matrix[x2][y2]

        counter = 0

        for row in matrix:
            # find the biggest number lower than our min
            lb, rb = 0, cols - 1
            while lb <= rb:
                mb = lb + (rb - lb) // 2

                if row[mb] < small_number:
                    lb = mb + 1
                else:
                    rb = mb - 1
                

            counter += lb

            lb, rb = 0, cols - 1
            while lb <= rb:
                mb = lb + (rb - lb) // 2

                if row[mb] <= big_number:
                    lb = mb + 1
                else:
                    rb = mb - 1

            counter += cols - lb 

        return counter 
 
# matrix = [
#     [1, 3, 7, 10, 15, 20],
#     [2, 6, 9, 14, 22, 25],
#     [3, 8, 10, 15, 25, 30],
#     [10, 11, 12, 23, 30, 35],
#     [20, 25, 30, 35, 40, 45]
# ]
#
#
# point1 = (1, 1)
# point2 = (3, 3)

solution = Solution()

N, M = 1000, 1000

matrix = [[random.randint(0, 10) for _ in range(M)]]
for _ in range(1, N):
    # ensure each element is bigger than previous one
    new_row = [random.randint(matrix[-1][0], matrix[-1][0] + 10)]
    for _ in range(1, M):
        new_row.append(random.randint(new_row[-1], new_row[-1] + 10))
    matrix.append(new_row)

point1 = (random.randint(0, N//2), random.randint(0, M//2))
point2 = (random.randint(N//2, N-1), random.randint(M//2, M-1))

start_time = time.perf_counter()
result1 = solution.find_min_max_from_matrix_naive(matrix, point1, point2)
end_time = time.perf_counter()
print(f"for naive, the time is {end_time - start_time}s")

start_time = time.perf_counter()
result2 = solution.find_min_max_from_matrix(matrix, point1, point2)
end_time = time.perf_counter()
print(f"for optimized, the time is {end_time - start_time}s")

