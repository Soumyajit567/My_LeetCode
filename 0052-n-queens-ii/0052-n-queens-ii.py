class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(row, col, queens):
            for queen in queens:
                r,c = queen
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return False
            return True
        def backtrack(row, queens):
            if row == n:
                return 1
            else:
                count = 0 
                for col in range(n):
                    if can_place(row, col, queens):
                        queens.append((row, col))
                        count += backtrack(row + 1, queens)
                        queens.pop()
            return count
        
        return backtrack(0, [])