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