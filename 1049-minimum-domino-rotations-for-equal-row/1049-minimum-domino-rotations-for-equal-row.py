class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def count_rotations(x):
            rot_top = rot_bot = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf'), float('inf')
                if t != x:
                    rot_top += 1
                if b != x:
                    rot_bot += 1
            return rot_top, rot_bot

        candidates = {tops[0], bottoms[0]}
        best = float('inf')
        for x in candidates:
            rt, rb = count_rotations(x)
            best = min(best, rt, rb)
        
        return -1 if best == float('inf') else best