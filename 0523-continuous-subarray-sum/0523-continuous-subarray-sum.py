class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0 : -1}
        _sum = 0
        left = 0
        right = 0
        for i in range(len(nums)):
            right = i
            _sum += nums[right]
            remainder = _sum % k
            if remainder < 0:
                remainder += k
            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i
            
        return False
