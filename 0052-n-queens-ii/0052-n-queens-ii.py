class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(row, col, queens):
            for queen in queens:
                r, c = queen
                # Check if two queens are in the same row, column, or diagonal
                if r == row or c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtrack(row, queens):
            if row == n:
                return 1  # Valid configuration found
            count = 0
            for col in range(n):
                if can_place(row, col, queens):
                    # Make a move
                    queens.append((row, col))
                    # Recurse with this move made
                    count += backtrack(row + 1, queens)
                    # Undo the move (backtrack)
                    queens.pop()
            return count

        return backtrack(0, [])