class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_before = [0] * n
        a_after = [0] * n
        
        b_count = 0
        for i in range(n):
            b_before[i] = b_count
            if s[i] == 'b':
                b_count += 1
          
        a_count = 0
        for i in range(n-1, -1, -1):
            a_after[i] = a_count
            if s[i] == 'a':
                a_count += 1
        

        min_deletions = float('inf')
        for i in range(n):
            min_deletions = min(min_deletions, b_before[i] + a_after[i])
        
        return min(min_deletions, a_count)  

