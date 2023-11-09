class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        count = 1  
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1  #
            else:
                total += count * (count + 1) // 2  
                count = 1  
                
        total += count * (count + 1) // 2  
        
        return total % (10**9 + 7)  

        
            
