class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute prime scores up to max(nums)
        maxv = max(nums)
        prime_score = [0] * (maxv + 1)
        for i in range(2, maxv + 1):
            if prime_score[i] == 0:  # i is prime
                for j in range(i, maxv + 1, i):
                    prime_score[j] += 1

        # Build arrays of blocking indices using monotonic stack
        prev_block = [-1] * n
        next_block = [n] * n

        # On left: find previous index j such that
        # prime_score[nums[j]] > prime_score[nums[i]] OR
        # prime_score equal and j < i (so equal score with smaller index blocks)
        stack = []
        for i in range(n):
            while stack:
                pj = stack[-1]
                if (prime_score[nums[pj]] > prime_score[nums[i]] or
                    (prime_score[nums[pj]] == prime_score[nums[i]] and pj < i)):
                    break
                stack.pop()
            prev_block[i] = stack[-1] if stack else -1
            stack.append(i)

        # On right: find next index j such that it blocks i (same logic)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack:
                pj = stack[-1]
                if (prime_score[nums[pj]] > prime_score[nums[i]] or
                    (prime_score[nums[pj]] == prime_score[nums[i]] and pj < i)):
                    break
                stack.pop()
            next_block[i] = stack[-1] if stack else n
            stack.append(i)

        # Prepare list of candidates: (value, count available, index)
        items = []
        for i in range(n):
            left_choices = i - prev_block[i]
            right_choices = next_block[i] - i
            cnt = left_choices * right_choices  # number of subarrays where i is chosen
            if cnt > 0:
                items.append((nums[i], cnt, i))

        # Sort by value descending (we want largest multipliers first)
        items.sort(key=lambda x: -x[0])

        def mod_pow(x, e):
            res = 1
            x %= MOD
            while e:
                if e & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                e >>= 1
            return res

        score = 1
        remaining = k
        for val, avail, _ in items:
            if remaining == 0:
                break
            take = min(avail, remaining)
            score = (score * mod_pow(val, take)) % MOD
            remaining -= take

        return score