class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mid = n // 2
        f = collections.defaultdict(int)
        f2 = collections.defaultdict(int)
        i = 0
        while i < mid:
            diff = abs(nums[i] - nums[~i]) 
            if diff not in f:
                f[diff] = 1
            else:
                f[diff] += 1
            left_n = nums[i]
            comp_left = k - nums[i]
            right_n = nums[~i]
            comp_right = k - nums[~i]
            max_left = max(left_n, comp_left)
            max_right = max(right_n, comp_right)
            key = max(max_left, max_right)
            if key not in f2:
                f2[key] = 1
            else:
                f2[key] += 1
            i += 1
        MAX = 10 ** 5
        count = 0
        best = MAX
        for i in range(k + 1):
            if i - 1 >= 0:
                count += f2[i - 1]
            best = min(best, count + (mid - f[i]))
        return best