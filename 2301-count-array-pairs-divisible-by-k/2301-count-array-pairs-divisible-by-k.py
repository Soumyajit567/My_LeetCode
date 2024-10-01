class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def prime_factors(n):
            i = 2
            factors = defaultdict(int)
            while i * i <= n:
                count = 0
                while n % i == 0:
                    n //= i
                    count += 1
                if count > 0:
                    factors[i] = count
                i += 1
            if n > 1:
                factors[n] += 1
            return factors

        k_factors = prime_factors(k)
        primes = list(k_factors.keys())
        k_exponents = [k_factors[p] for p in primes]
        m = len(primes)

        def get_exponent_profile(num):
            exponents = []
            for i in range(m):
                p = primes[i]
                e = 0
                while num % p == 0:
                    num //= p
                    e += 1
                exponents.append(min(e, k_exponents[i]))
            return tuple(exponents)

        counts = defaultdict(int)
        exponent_profiles = []

        for num in nums:
            ep = get_exponent_profile(num)
            exponent_profiles.append(ep)
            counts[ep] += 1


        total_pairs = 0
        exponent_profiles_set = list(counts.keys())

        for i in range(len(exponent_profiles_set)):
            ep1 = exponent_profiles_set[i]
            counts_ep1 = counts[ep1]
            for j in range(i, len(exponent_profiles_set)):
                ep2 = exponent_profiles_set[j]
                counts_ep2 = counts[ep2]
                sum_exponents = [ep1[x] + ep2[x] for x in range(m)]
                if all(sum_exponents[x] >= k_exponents[x] for x in range(m)):
                    if i == j:
                        total_pairs += counts_ep1 * (counts_ep1 - 1) // 2
                    else:
                        total_pairs += counts_ep1 * counts_ep2

        return total_pairs