class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Calculate prime scores for all numbers
        def get_prime_score(num):
            if num <= 1:
                return 0
            count = 0
            # Check for factor 2
            if num % 2 == 0:
                count += 1
                while num % 2 == 0:
                    num //= 2
            # Check for odd factors
            i = 3
            while i * i <= num:
                if num % i == 0:
                    count += 1
                    while num % i == 0:
                        num //= i
                i += 2
            # If num > 1, then it's a prime factor
            if num > 1:
                count += 1
            return count
        
        prime_scores = [get_prime_score(num) for num in nums]
        
        # For each index i, find the range where nums[i] can be selected
        # Left[i] = leftmost index where nums[i] has highest prime score
        # Right[i] = rightmost index where nums[i] has highest prime score
        
        # Find left boundaries (nearest element to the left with prime_score > prime_scores[i])
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # Find right boundaries (nearest element to the right with prime_score >= prime_scores[i])
        # We use >= to handle ties (smaller index wins)
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        # Calculate how many times each element can be selected
        # Element at index i can be selected in subarrays [l, r] where:
        # left[i] < l <= i and i <= r < right[i]
        contributions = []
        for i in range(n):
            left_count = i - left[i]  # number of valid left boundaries
            right_count = right[i] - i  # number of valid right boundaries
            times = left_count * right_count
            contributions.append((nums[i], times))
        
        # Sort by value in descending order
        contributions.sort(reverse=True)
        
        # Greedily select the largest values
        score = 1
        operations = 0
        
        for value, times in contributions:
            if operations >= k:
                break
            # Take min(times, k - operations) of this value
            take = min(times, k - operations)
            # Multiply score by value^take
            score = (score * pow(value, take, MOD)) % MOD
            operations += take
        
        return score