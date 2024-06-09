class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod_count = {0: 1}
        total_sum = 0
        count = 0
        
        for num in nums:
            total_sum += num
            mod = total_sum % k
            if mod < 0:
                mod += k
            
            if mod in prefix_mod_count:
                count += prefix_mod_count[mod]
                prefix_mod_count[mod] += 1
            else:
                prefix_mod_count[mod] = 1
        
        return count
                
            
        