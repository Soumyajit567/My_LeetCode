class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod_index = {0: -1}
        total_sum = 0
        
        for i, num in enumerate(nums):
            total_sum += num
            mod = total_sum % k
            
           
            if mod < 0:
                mod += k
                
            if mod in prefix_mod_index:
                if i - prefix_mod_index[mod] > 1:  
                    return True
            else:
                prefix_mod_index[mod] = i
        
        return False