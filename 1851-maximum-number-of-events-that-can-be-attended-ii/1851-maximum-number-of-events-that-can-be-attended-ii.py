from heapq import heappop, heappush

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])  # Sort by end time
        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]
        
        for i in range(1, len(events) + 1):
            for j in range(1, k + 1):
                # Find the previous non-overlapping event using binary search
                prev_idx = self.findPrev(events, i - 1)
                
                # DP transition
                dp[i][j] = max(dp[i - 1][j], dp[prev_idx + 1][j - 1] + events[i - 1][2])
        
        return max(dp[-1])

    def findPrev(self, events, idx):
        # Binary search to find the previous non-overlapping event
        left, right = 0, idx 
        target = events[idx][0]
        while left <= right:
            mid = (left + right) // 2
            if events[mid][1] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1







