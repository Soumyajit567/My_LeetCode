class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        n_diffs = math.ceil(n / 2)

        # Find the counts for the symetrical differences.        
        diff_counts = defaultdict(int)
        for i in range(n_diffs):
            diff = abs(nums[i] - nums[~i])
            diff_counts[diff] += 1

        # Find the counts for the cost 1 thresholds
        cost_1_threshold_counts = defaultdict(int)
        for i in range(n_diffs):
            l = min(nums[i], nums[~i])
            h = max(nums[i], nums[~i])
            cost_1_threshold = max(h, k-l)
            cost_1_threshold_counts[cost_1_threshold] += 1

        # Calculate the cost for each possible value of x.
        min_cost = math.inf
        n_cost_2 = 0
        for x in range(k+1):
            cur_cost = n_diffs + n_cost_2 - diff_counts[x] 

            min_cost = min(min_cost, cur_cost)

            n_cost_2 += cost_1_threshold_counts[x]
        
        return min_cost