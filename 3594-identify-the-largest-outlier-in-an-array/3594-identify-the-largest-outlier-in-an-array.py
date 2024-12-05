class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        for idx, val in enumerate(nums):
            hashmap[val] = idx
        total_sum = sum(nums)
        res = float("-inf")
        for i, v in enumerate(nums):
            curr_sum = total_sum - v
            if curr_sum % 2 == 0:
                val = curr_sum // 2
                if val in hashmap and hashmap[val] != i:
                    res = max(res, v)
        return res

