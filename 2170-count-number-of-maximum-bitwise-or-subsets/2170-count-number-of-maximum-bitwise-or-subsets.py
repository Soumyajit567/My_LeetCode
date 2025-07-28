class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        
        # Calculate the maximum bitwise OR by iterating through all subsets
        for i in range(1 << n):
            current_or = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    current_or |= nums[j]
            max_or = max(max_or, current_or)
        
        # Count the number of subsets that have the maximum bitwise OR
        count = 0
        for i in range(1 << n):
            current_or = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    current_or |= nums[j]
            if current_or == max_or:
                count += 1
                
        return count
