class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        max_deltas, deltas = [], []

        for i in range(len(nums) // 2):
            max_delta = max(nums[i], nums[~i], k - min(nums[i], nums[~i]))
            max_deltas.append(max_delta)
            deltas.append(abs(nums[i] - nums[~i]))

        max_deltas.sort()
        counter = Counter(deltas)
        changes = float("inf")

        for target_delta, count in counter.items():
            ones_start = bisect_left(max_deltas, target_delta)
            cur_changes = -count + ones_start * 2 + (len(max_deltas) - ones_start)
            changes = min(changes, cur_changes)
        return changes