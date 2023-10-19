class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = min_prod = result = nums[0]
        for i in range(1, n):
            temp_max  = max(max_prod * nums[i], nums[i], min_prod  * nums[i])
            min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])

            max_prod = temp_max            

            result = max(result, max_prod)
        return result