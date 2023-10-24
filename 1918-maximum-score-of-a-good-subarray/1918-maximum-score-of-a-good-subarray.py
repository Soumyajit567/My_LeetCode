class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            def binary_search(arr, x):
                low, high = 0, len(arr) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if arr[mid] < x:
                        low = mid + 1
                    else:
                        high = mid - 1
                return low

            n = len(nums)
            left = [0] * k
            curr_min = inf
            for i in range(k - 1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left[i] = curr_min

            right = []
            curr_min = inf
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            ans = 0
            for j in range(len(right)):
                curr_min = right[j]
                i = binary_search(left, curr_min)
                size = (k + j) - i + 1
                ans = max(ans, curr_min * size)
                
            return ans
        
        return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))