class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_left_time = max(left) if left else 0
        max_right_time = max([n - pos for pos in right]) if right else 0
        return max(max_left_time, max_right_time)