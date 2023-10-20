class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<unordered_set<char>> rows(m), cols(n), squares(9);
        vector<pair<int, int>> stack;

        // Lambda function for the backtracking
        function<bool(int)> backtracking = [&](int pos) -> bool {
            if (pos == stack.size()) return true;  // If there are no more positions on stack, we solved the puzzle

            auto [i, j] = stack[pos];
            int squareIndex = (i / 3) * 3 + (j / 3);
            
            for (char num = '1'; num <= '9'; ++num) {
                if (rows[i].count(num) || cols[j].count(num) || squares[squareIndex].count(num))
                    continue;  // Skip if number is already in the row, column, or square

                board[i][j] = num;
                rows[i].insert(num);
                cols[j].insert(num);
                squares[squareIndex].insert(num);

                if (backtracking(pos + 1)) return true;

                // Undo the move
                board[i][j] = '.';
                rows[i].erase(num);
                cols[j].erase(num);
                squares[squareIndex].erase(num);
            }
            return false;  // No suitable number was found
        };

        // Initialize sets and stack
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == '.') {
                    stack.emplace_back(i, j);
                } else {
                    char num = board[i][j];
                    rows[i].insert(num);
                    cols[j].insert(num);
                    squares[(i / 3) * 3 + (j / 3)].insert(num);
                }
            }
        }

        backtracking(0);
    
    }
};