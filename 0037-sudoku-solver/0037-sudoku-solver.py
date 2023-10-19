class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)
        stack = []
        def backtracking(board):
            nonlocal rows
            nonlocal cols
            nonlocal square
            nonlocal stack
            if not stack:
                return True
            i, j = stack[-1]
            for num in range(1, 10):
                num_str = str(num)
                if num_str not in rows[i] and num_str not in cols[j] and num_str not in square[(i // 3, j // 3)]:
                    board[i][j] = num_str
                    rows[i].add(num_str)
                    cols[j].add(num_str)
                    square[(i // 3, j // 3)].add(num_str)
                    stack.pop()
                    if backtracking(board):
                        return True
                    board[i][j] = "."
                    rows[i].remove(num_str)
                    cols[j].remove(num_str)
                    square[(i // 3, j // 3)].remove(num_str)
                    stack.append((i, j))
            return False
                    


        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    stack.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])
        

        backtracking(board)
        return board

        