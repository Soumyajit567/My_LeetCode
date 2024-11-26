class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        res = right

        left = 0
        while left < right:
            while right < n and arr[right] < arr[left]:
                right += 1
            res = min(res, right - left - 1)
            if arr[left] > arr[left + 1]:
                break
            left += 1
        return res