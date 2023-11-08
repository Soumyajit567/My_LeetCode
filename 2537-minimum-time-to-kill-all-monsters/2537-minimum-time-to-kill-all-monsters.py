class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)

        power.sort()

        @lru_cache(None)
        def dfs(bitmask,gain):
            if bitmask == (1<<n) - 1:
                return 0

            min_val = float("inf")

            for i in range(n):
                if not (1<<i)&bitmask:
                    min_val = min(min_val,math.ceil(power[i]/gain) + dfs(bitmask|(1<<i),gain+1))

            return min_val

        return dfs(0,1)