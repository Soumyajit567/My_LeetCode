class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        total_sum = 0
        current_max = maximumHeight[0]  
        
        for height in maximumHeight:
            assigned_height = min(height, current_max)
            if assigned_height < 1:
                return -1
            
            total_sum += assigned_height
            
            current_max = assigned_height - 1
        
        return total_sum