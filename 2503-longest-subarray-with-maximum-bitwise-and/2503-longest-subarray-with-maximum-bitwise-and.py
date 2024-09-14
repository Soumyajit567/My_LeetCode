class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAnd = max(nums)
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != maxAnd :
                l = r+1
            res = max(res,r-l+1)
        return res


"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = cur = mx = 0
        for num in nums:
            if num > mx:
                mx = num
                longest = cur = 1
            elif num == mx:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 0    
        return longest
"""