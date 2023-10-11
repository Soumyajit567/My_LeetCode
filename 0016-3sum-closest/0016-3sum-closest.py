class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff = float("inf")
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(target-total) < abs(diff):
                    diff = target - total
                if total < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0: break
        return target - diff