class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = collections.defaultdict(int)
        for i, v in enumerate(nums):
            s[v] = i
        total = sum(nums)
        res = float('-inf')
        for i,num in enumerate(nums):
            curr_sum = total - num
            if curr_sum%2 == 0: 
                val = curr_sum // 2
                if val in s and s[val] != i:
                    res = max(res, num)
        return res