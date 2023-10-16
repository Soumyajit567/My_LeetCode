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
