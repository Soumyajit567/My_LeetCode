class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n, m = len(grid), len(grid[0])
        Ans = [row[:] for row in grid]  # Create a copy of the input matrix
        
        for i in range(n):
            for j in range(m):
                Ans[i][j] = 1
        
        Mul = 1
        for i in range(n):
            for j in range(m):
                Ans[i][j] = (Ans[i][j] * Mul) % mod
                Mul = (Mul * grid[i][j]) % mod
        
        Mul = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                Ans[i][j] = (Ans[i][j] * Mul) % mod
                Mul = (Mul * grid[i][j]) % mod
        
        return Ans