class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        n = len(cost)
        @cache
        def memo(i, t):
            if t <= 0:
                return 0
            elif i == n:
                return float("inf")
            elif (i, t) in dp:
                return dp[(i, t)]
            else:
                paint = cost[i] +  memo(i + 1, t - 1 - time[i])
                dont_paint = memo(i + 1, t)
                return min(paint, dont_paint)

        return memo(0, n)

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[n][i] = inf

        for i in range(n - 1, -1, -1):
            for remain in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)
        
        return dp[0][n]



"""
Initialization:

dp is a 2D list where dp[i][remain] represents the minimum cost to paint from the i-th wall to the end, with remain walls remaining to be considered.
When no walls are left (i == n), the costs are set to infinity because it's impossible to paint any more walls.


Transitions:

For each wall from n-1 to 0 (inclusive), and for each remaining count from 1 to n (inclusive), we consider two possibilities:
We paint the current wall, which incurs a cost of cost[i] and potentially paints some number of walls based on time[i]. The remaining count decreases by at least 1 (because we've painted the current wall), and potentially more, based on time[i].
We don't paint the current wall, so we carry over the cost from the next wall (dp[i + 1][remain]).

Result:

After filling in the DP table, dp[0][n] gives the minimum cost to consider all walls while starting with all of them remaining.
A few key points to consider for correctness and efficiency:

The inner loop's range starts from 1 because having 0 walls remaining doesn't make practical sense when we're considering whether to paint a wall.

The use of max(0, remain - 1 - time[i]) ensures we don't look up a negative index, which would happen if remain - 1 - time[i] is less than 0. However, it's crucial that the logic ensures correctness in the case when time[i] is more than remain - 1. This situation implies that more walls were painted due to the time spent on the current wall, and the code seems to assume that it's the same as not painting those extra walls. If the problem statement considers the time spent on each wall as mandatory (i.e., you have to spend the whole time[i] on wall i even if it results in more walls being painted), this logic is correct.

Ensure that the indexing used in the cost and time lists corresponds correctly to the problem's specifications regarding whether the indexing is 0-based or 1-based.
The code logic appears sound based on the inferred problem statement. However, make sure to test this solution against various test cases, especially edge cases, to verify its correctness fully.



"""