class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # A mountain must have at least 3 points

        max_length = 0
        i = 1  # Start from 1 because we need to compare with the previous item

        while i < n:
            # Find the start of the ascent
            while i < n and nums[i - 1] >= nums[i]:
                i += 1

            up_len = 0
            # Climb the mountain
            while i < n and nums[i - 1] < nums[i]:
                i += 1
                up_len += 1

            down_len = 0
            # Go down the mountain
            while i < n and nums[i - 1] > nums[i]:
                i += 1
                down_len += 1

            # If we have a valid sequence, update max_length
            if up_len > 0 and down_len > 0:
                max_length = max(max_length, up_len + down_len + 1)

        return max_length