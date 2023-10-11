class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = sorted(set(nums))

        count = len(nums)
        p1,p2 = 0,0

        while p1 < len(nums) and p2 < len(n):
            while p2 < len(n) and n[p2] < n[p1] + len(nums):
                p2 += 1
            count = min(count, len(nums) - p2 + p1)
            p1 += 1
            
        return count



"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        
        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans
"""