class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
                if sx == fx and sy == fy:
                    if t == 1:
                        return False
                    else:
                        return True
                return abs(sx - fx) <= t and abs(sy - fy) <= t