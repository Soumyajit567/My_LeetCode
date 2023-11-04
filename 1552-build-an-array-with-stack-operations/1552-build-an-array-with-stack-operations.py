class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        out = []
        target.sort()
        for i in range(1, n + 1):
            if stack and stack[-1] not in target:
                stack.pop()
                out.append("Pop")
            if stack and stack[-1] == target[-1]:
                return out
            stack.append(i)
            out.append("Push")
        return out