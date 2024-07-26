class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, bottom, left, right = float('inf'), -float('inf'), float('inf'), -float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
    
        height = bottom - top + 1
        width = right - left + 1
        return height * width
