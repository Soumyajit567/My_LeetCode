class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        result = []
        
        for q in queries:
            idx = bisect.bisect_left(nums, q)
            
            if idx > 0:
                left_cost = q * idx - prefix_sum[idx - 1]
            else:
                left_cost = 0
            
            if idx < n:
                right_cost = (prefix_sum[n - 1] - (prefix_sum[idx - 1] if idx > 0 else 0)) - q * (n - idx)
            else:
                right_cost = 0
            
            result.append(left_cost + right_cost)
        
        return result