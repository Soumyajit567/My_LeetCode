class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        count = 0
        divisor = 2
        
        while n > 1:
            while n % divisor == 0:
                count += divisor
                n //= divisor
            divisor += 1
        
        return count