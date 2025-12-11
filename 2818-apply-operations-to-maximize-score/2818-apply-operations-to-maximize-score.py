from typing import List

MOD = 10**9 + 7

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0: 
            return 1

        maxA = max(nums)
        # Sieve for smallest prime factor (SPF)
        spf = list(range(maxA + 1))
        for p in range(2, int(maxA**0.5) + 1):
            if spf[p] == p:
                step = p
                start = p * p
                for multiple in range(start, maxA + 1, step):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # function to count distinct prime factors using spf
        def distinct_pf(x: int) -> int:
            last = 0
            cnt = 0
            while x > 1:
                p = spf[x]
                if p != last:
                    cnt += 1
                    last = p
                while x % p == 0:
                    x //= p
            return cnt

        # prime scores array
        ps = [distinct_pf(v) for v in nums]

        # compute previous greater (or equal with smaller index) L: index of last element to left
        L = [-1] * n
        stack = []
        for i in range(n):
            # while top has prime-score < current's prime-score OR
            # prime-score == current's prime-score and top index > i (we want smaller index to win,
            # so those with smaller index should be considered "greater or equal" so they block).
            # For previous greater we pop while top's prime-score < current prime-score
            # or (top's prime-score == current and top index > current) - but top index is always < i, so tie handled by not popping when equal.
            while stack and ps[stack[-1]] < ps[i]:
                stack.pop()
            # If equal prime-score, we should keep previous (smaller index) to block current.
            L[i] = stack[-1] if stack else -1
            stack.append(i)

        # compute next greater to right: R index of next element to right that blocks i
        R = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            # For right side, we pop while top's prime-score <= current's prime-score
            # because if equal prime-score, the smaller index (which is current when scanning right to left)
            # should win, so the right element with equal score must be considered as blocked by current,
            # thus it should not block current; so for current we need first index to right with strictly greater prime-score
            # or equal but smaller index (which cannot be because right index > current), so we pop when ps[top] <= ps[i].
            while stack and ps[stack[-1]] <= ps[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)

        # Each index i can be chosen cnt = (i - L[i]) * (R[i] - i) times
        items = []
        for i in range(n):
            cnt = (i - L[i]) * (R[i] - i)
            items.append((nums[i], cnt))

        # Sort items descending by value so we take biggest nums first
        items.sort(key=lambda x: -x[0])

        # Greedily use counts up to k
        res = 1
        rem = k
        for val, cnt in items:
            if rem == 0:
                break
            use = cnt if cnt <= rem else rem
            # modular exponentiation
            res = (res * pow(val, use, MOD)) % MOD
            rem -= use

        return res
