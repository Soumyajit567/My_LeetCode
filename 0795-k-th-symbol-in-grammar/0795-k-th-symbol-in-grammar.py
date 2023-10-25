class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        # Determine parent in the previous row
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        # If k is odd and parent is 0 or if k is even and parent is 1
        return parent if k % 2 == 1 else 1 - parent