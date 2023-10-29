class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve of eratosthenes
        primes = [2]
        for i in range(2, 1001):
            c = 0
            for j in range(2, (int)(math.sqrt(i))+1):
                if i%j == 0: c+=1
            if c == 0: primes.append(i)

        # Traversing from back and using binary search to find a suitable primes no. to subtract
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 2 and nums[i + 1] <= 2: return False
            if nums[i] >= nums[i + 1]:
                n = nums[i] - nums[i + 1] + 1
                indx = bisect.bisect_left(primes, n)
                if indx >= len(primes): return False
                if primes[indx] >= nums[i]: return False
                nums[i]-=primes[indx]
                if nums[i] >= nums[i + 1]: return False
        return True
