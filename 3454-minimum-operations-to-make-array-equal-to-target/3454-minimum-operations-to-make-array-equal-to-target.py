class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        def f(x):
            ans = [x[0]]
            for i in range(1, len(x)):
                ans.append(x[i] - x[i-1])
            ans.append(-x[-1])
            return ans
        v1 = f(nums)
        v2 = f(target)
        return sum(x - y if x > y else 0 for x, y in zip(v1, v2))