class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  # Sort by start day
        n = len(events)
        
        # dp[i][j] = max value from events[i:] with j events left
        dp = [[-1] * (k + 1) for _ in range(n + 1)]
        
        def binary_search(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def dfs(i, k):
            if k == 0 or i >= n:
                return 0
            if dp[i][k] != -1:
                return dp[i][k]
            
            # Skip current event
            max_value = dfs(i + 1, k)
            
            # Take current event
            next_idx = binary_search(events[i][1])  # Find next non-overlapping event
            max_value = max(max_value, events[i][2] + dfs(next_idx, k - 1))
            
            dp[i][k] = max_value
            return max_value
        
        return dfs(0, k)