class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        while time > 0:
            for i in range(1, n):
                if time == 0:
                    return i
                time -= 1
            for i in range(n, 1, -1):
                if time == 0:
                    return i
                time -= 1
        return 1