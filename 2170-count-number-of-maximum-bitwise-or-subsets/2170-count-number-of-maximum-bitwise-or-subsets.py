class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Split array into two halves
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Compute OR values and their counts for left half
        left_ors = defaultdict(int)
        for i in range(1 << len(left)):
            current_or = 0
            for j in range(len(left)):
                if i & (1 << j)!= 0:
                    current_or |= left[j]
            left_ors[current_or] += 1 
        print(left_ors)
        print("     ")
        
        # Compute OR values and their counts for right half
        right_ors = defaultdict(int)
        for i in range(1 << len(right)):
            current_or = 0
            for j in range(len(right)):
                if i & (1 << j)!= 0:
                    current_or |= right[j]
            right_ors[current_or] += 1
        print(right_ors)
        print("       ")
        
        # Find maximum OR by combining left and right
        max_or = 0
        for l in left_ors:
            for r in right_ors:
                max_or = max(max_or, l | r)
        
        # Count subsets with maximum OR
        count = 0
        for l in left_ors.keys():
            for r in right_ors.keys():
                if (l | r) == max_or:
                    count += left_ors[l] * right_ors[r]
                    print(count)
        
        return count