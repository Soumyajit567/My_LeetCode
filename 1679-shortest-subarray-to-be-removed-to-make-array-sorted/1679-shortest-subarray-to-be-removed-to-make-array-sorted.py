class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        
        res = n - left - 1
        right = n - 1
        while right > left:
            while left >= 0 and arr[right] < arr[left]:
                left -= 1
            res = min(res, right - left - 1)
            if arr[right] < arr[right - 1]:
                break
            right -= 1
        return res