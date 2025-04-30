class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        n = len(questions) - 1

        @cache
        def memo(i, j):
            if i > j:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            else:
                max_val = max(questions[i][0] + memo(i + questions[i][1] + 1, j), memo(i + 1 , j))
                dp[(i ,j)] = max_val
                return dp[(i, j)]
        
        return memo(0, len(questions) - 1)