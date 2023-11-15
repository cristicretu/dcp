"""
15.11.2023

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

class Solution:
    def no_of_ways(self, rows: int, columns: int) -> int:
        if rows < 1:
            raise ValueError("Matrix should not be empty")

        if columns < 1:
            raise ValueError("Matrix should also have columns")

        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        # Base case
        dp[0][0] = 1

        for i in range(rows):
            for j in range(columns):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

       return dp[rows - 1][columns - 1]

solution = Solution()
print(solution.no_of_ways(5, 5))

