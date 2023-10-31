class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        max_cost = 0
        curr_cost = 0
        
        char_val_dict = {char: val for char, val in zip(chars, vals)}
        
        for char in s:
            if char in char_val_dict:
                curr_cost += char_val_dict[char]
            else:
                curr_cost += ord(char) - 96  
            
            if curr_cost < 0: 
                curr_cost = 0
                
            max_cost = max(max_cost, curr_cost)  
        
        return max_cost
                