class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        odd_count = 0
        prefix_count = {0: 1}

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1

            if odd_count - k in prefix_count:
                ans += prefix_count[odd_count - k]

            if odd_count in prefix_count:
                prefix_count[odd_count] += 1
            else:
                prefix_count[odd_count] = 1

        return ans
