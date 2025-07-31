class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = {0} 
        for num in arr:
            next_set = {num}  
            for prev_or in curr:
                next_set.add(prev_or | num)  
            curr = next_set
            result.update(curr)  
        return len(result)