class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        divisors = []
        for i in range(1, int(k**0.5) + 1):
            if k % i == 0:
                divisors.append(i)
                if i != k // i:
                    divisors.append(k // i)
        divisors.sort()
        divisor_indices = {d: i for i, d in enumerate(divisors)}
        
        # Step 2: Count occurrences of gcds
        counts = [0] * len(divisors)
        for num in nums:
            num_gcd = gcd(num, k)
            idx = divisor_indices[num_gcd]
            counts[idx] += 1
        
        # Step 3: Count valid pairs
        res = 0
        for i in range(len(divisors)):
            d1 = divisors[i]
            c1 = counts[i]
            if c1 == 0:
                continue
            for j in range(i, len(divisors)):
                d2 = divisors[j]
                c2 = counts[j]
                if c2 == 0:
                    continue
                if (d1 * d2) % k == 0:
                    if i == j:
                        # Avoid double counting when d1 == d2
                        res += c1 * (c1 - 1) // 2
                    else:
                        res += c1 * c2
        return res