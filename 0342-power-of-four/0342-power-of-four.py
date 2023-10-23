class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        log_base_4 = math.log(n, 4)
        
        return log_base_4 == int(log_base_4)