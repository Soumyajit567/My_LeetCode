class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dfs(i):
            if i == 1:
                return 0
            elif i % 2 == 0:
                return 1 + dfs(i // 2)
            else:
                return 1 +  min(dfs(i + 1), dfs(i - 1))
        return dfs(n)


