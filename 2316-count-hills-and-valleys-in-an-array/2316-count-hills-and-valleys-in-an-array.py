class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            # Skip if nums[i] is the same as the previous
            if nums[i] == nums[i - 1]:
                continue

            # Find left neighbor that's not equal to nums[i]
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Find right neighbor that's not equal to nums[i]
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1

            # Check if both neighbors exist
            if left >= 0 and right < n:
                if nums[left] < nums[i] > nums[right]:  # hill
                    count += 1
                elif nums[left] > nums[i] < nums[right]:  # valley
                    count += 1

        return count