class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = collections.defaultdict(int)
        
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        for num in arr:
            remainder = num % k
            
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                complement = k - remainder
                if remainder_count[remainder] != remainder_count[complement]:
                    return False
        
        return True