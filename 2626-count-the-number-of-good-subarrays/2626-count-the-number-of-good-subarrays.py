class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
            # Helper function to find the number of pairs with count >= 2
        def count_pairs(count):
            return comb(count, 2) if count >= 2 else 0

        n = len(nums)
        answer = 0
        prefix_sum = defaultdict(int)
        total_pairs = 0

        # Start and end pointers for the sliding window
        start = 0
        end = 0

        for start in range(n):
            # Move the end of the window to the right until we have at least k pairs
            while end < n and total_pairs < k:
                prefix_sum[nums[end]] += 1
                total_pairs += count_pairs(prefix_sum[nums[end]]) - count_pairs(prefix_sum[nums[end]] - 1)
                end += 1

            # If we have at least k pairs, all subarrays starting at `start` and ending from `end` to `n - 1` are good
            if total_pairs >= k:
                answer += n - end + 1

            # Move the start of the window to the right, and update the total pairs
            total_pairs -= count_pairs(prefix_sum[nums[start]]) - count_pairs(prefix_sum[nums[start]] - 1)
            prefix_sum[nums[start]] -= 1

        return answer