class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_value
        return moves