class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        cummulative = pref[0]
        
        for i in range(1, len(pref)):
            operand = cummulative ^ pref[i]
            pref[i] = operand
            cummulative ^= operand
            
        return pref