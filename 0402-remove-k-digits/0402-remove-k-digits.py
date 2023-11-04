class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If we need to remove all digits, return "0"
        if len(num) == k:
            return "0"

        stack = []
        for digit in num:
            # While there is a digit to remove and the last digit in stack is greater than the current one
            # which means by removing the last digit in stack we can get a smaller number
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If there are still digits to remove, remove them from the end
        stack = stack[:-k] if k else stack

        # Convert stack to string and strip leading zeros
        return ''.join(stack).lstrip('0') or "0"  # Ensure we don't return an empty string



"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        def dfs(index, removed, path):
            # If we have removed k digits, add the current number to the result
            if removed == k:
                res.append(int(''.join(map(str, path)) + num[index:]))
                return
            if index == len(num):
                return

            # Option 1: remove the current digit
            if removed < k:
                dfs(index + 1, removed + 1, path)

            # Option 2: keep the current digit
            dfs(index + 1, removed, path + [num[index]])

        res = []
        dfs(0, 0, [])
        return str(min(res))
"""