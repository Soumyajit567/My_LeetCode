from sortedcontainers import SortedList

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        S = SortedList()  # Using SortedList to maintain a sorted order of pairs.
        
        for i in range(n):
            if i >= indexDifference:
                x = i - indexDifference
                y = nums[x]
                S.add((y, x))  # Adding a tuple instead of a pair.
                
            # Searching for the lower bound in the sorted list.
            it = S.bisect_left((nums[i] + valueDifference, 0))
            if it != len(S):
                return [S[it][1], i]  # Accessing elements of a tuple.
            
            it = S.bisect_left((nums[i] - valueDifference + 1, 0))
            if it != 0:
                return [S[it - 1][1], i]  # Going one element back in the list.
                
        return [-1, -1]