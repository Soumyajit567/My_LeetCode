from functools import cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Remove the visited sets; they are not needed in this approach

        # Change dp1 and dp2 into a single dictionary for memoization.
        # This dictionary will hold the maximum cherries two robots can pick starting from (i, j) and (i, k) to the bottom.
        dp = {}

        @cache
        def dfs(i, j, k):
            # Check for out of bounds
            if i == m or j < 0 or j == n or k < 0 or k == n:
                return 0

            # If this state is already computed
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            # Cherries at the current positions of both robots
            # If they're at the same position, we shouldn't double-count the cherries.
            cherries = grid[i][j] + (grid[i][k] if j != k else 0)

            # Max cherries picked from this position to the end
            max_cherries = 0
            for dj in [1, 0, -1]:
                for dk in [1, 0, -1]:
                    # Consider all possible moves for both robots
                    nj, nk = j + dj, k + dk
                    max_cherries = max(max_cherries, dfs(i + 1, nj, nk))

            # Cherries picked from this cell plus max cherries picked from future moves
            answer = cherries + max_cherries

            # Save to the memoization dictionary
            dp[(i, j, k)] = answer
            return answer

        # Start the DFS from the top row, with robots at the leftmost and rightmost positions
        return dfs(0, 0, n - 1)






"""
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(row, col1, col2):
            # If we're outside the grid, we can't collect any cherries
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return 0
            
            # Current cell value: If robots are in the same cell, we only add the cherries once. 
            # Otherwise, we add cherries from both cells
            result = grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]

            # If we're not in the last row, we need to add cherries from the next row
            if row != m - 1:
                # Both robots can move to 3 adjacent cells: left, down, or right. 
                # We need to try all combinations of these moves
                result += max(dp(row + 1, new_col1, new_col2)
                              for new_col1 in [col1, col1 + 1, col1 - 1]
                              for new_col2 in [col2, col2 + 1, col2 - 1])
            
            return result

        # We start from row 0 with Robot #1 at column 0 and Robot #2 at column n-1
        return dp(0, 0, n - 1)
"""