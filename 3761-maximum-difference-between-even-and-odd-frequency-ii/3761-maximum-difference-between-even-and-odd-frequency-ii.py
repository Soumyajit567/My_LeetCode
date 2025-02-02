class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # Build prefix array P: 
        # P[i][d] = frequency of digit d (0 <= d < 5) in s[0:i]
        P = [[0]*5 for _ in range(n+1)]
        for i in range(n):
            d = ord(s[i]) - ord('0')
            # Copy the previous counts:
            P[i+1] = P[i][:]  
            P[i+1][d] += 1

        # For each digit d, record the FIRST index i at which a particular frequency appears.
        # (Because the prefix array is monotonic, if P[j][d] is X then any i >= the first occurrence of X
        # will have P[i][d] == X, and then the substring frequency would be 0.)
        first_occ = [dict() for _ in range(5)]
        for d in range(5):
            for i in range(n+1):
                f = P[i][d]
                if f not in first_occ[d]:
                    first_occ[d][f] = i

        INF = 10**9  # a large number; differences never exceed about 30000

        # Precompute dp arrays for each ordered pair (a, b) with a != b,
        # and for each parity combination (p_a, p_b) where:
        #    we want indices i with P[i][a] mod 2 == p_a and P[i][b] mod 2 == p_b.
        # Here dp[(a,b,p_a,p_b)][i] = min_{j=0..i} { P[j][a] - P[j][b] }
        # for those j that satisfy the parity condition; if not, we treat the candidate as INF.
        dp = {}
        for a in range(5):
            for b in range(5):
                if a == b: 
                    continue
                for p_a in (0, 1):
                    for p_b in (0, 1):
                        arr = [INF]*(n+1)
                        # For i = 0:
                        if (P[0][a] & 1) == p_a and (P[0][b] & 1) == p_b:
                            arr[0] = P[0][a] - P[0][b]
                        cur = arr[0]
                        for i in range(1, n+1):
                            candidate = INF
                            if (P[i][a] & 1) == p_a and (P[i][b] & 1) == p_b:
                                candidate = P[i][a] - P[i][b]
                            if candidate < cur:
                                cur = candidate
                            arr[i] = cur
                        dp[(a, b, p_a, p_b)] = arr

        ans = -10**9  # Initialize answer (it can be negative)
        # Now, iterate over possible ending positions j of the substring.
        # j represents the prefix endpoint so that the substring is s[i:j] for some i.
        # We require the substring length j - i >= k, so i can be at most j - k.
        for j in range(k, n+1):
            # For each candidate pair (a, b) with a != b, we consider using digit a for the odd frequency
            # and digit b for the even frequency.
            # We also require that digit a and digit b actually appear in s[i:j] (i.e. P[j][a] > 0 and P[j][b] > 0).
            for a in range(5):
                if P[j][a] == 0:
                    continue  # digit a must appear in s[i:j]
                for b in range(5):
                    if a == b:
                        continue
                    if P[j][b] == 0:
                        continue  # digit b must appear in s[i:j]
                    # For the substring frequency for a, we need:
                    #   (P[j][a] - P[i][a]) mod 2 = 1  <=>  P[i][a] mod 2 = 1 - (P[j][a] mod 2)
                    r_a = 1 - (P[j][a] & 1)
                    # For digit b we need:
                    #   (P[j][b] - P[i][b]) mod 2 = 0  <=>  P[i][b] mod 2 = P[j][b] mod 2
                    r_b = P[j][b] & 1

                    # Also, to have a positive frequency in the substring we must have:
                    #   P[i][a] < P[j][a]  and  P[i][b] < P[j][b].
                    # Because the prefix counts are non-decreasing,
                    # the set of indices i with P[i][d] < P[j][d] is exactly those i with i < (first_occ[d][P[j][d]]).
                    fa = first_occ[a].get(P[j][a], None)
                    fb = first_occ[b].get(P[j][b], None)
                    if fa is None or fb is None:
                        continue
                    # Among valid i, we must have i <= j-k (to ensure the substring has length >= k)
                    # and also i < fa and i < fb.
                    R = j - k
                    R = min(R, fa - 1, fb - 1)
                    if R < 0:
                        continue

                    # Query the precomputed dp array for the best (smallest) candidate value among i in [0, R].
                    candidate = dp[(a, b, r_a, r_b)][R]
                    if candidate == INF:
                        continue
                    # Then for this j, a, b, one valid substring s[i:j] has difference:
                    #    (P[j][a]-P[j][b]) - (P[i][a]-P[i][b])
                    diff = (P[j][a] - P[j][b]) - candidate
                    if diff > ans:
                        ans = diff
        return ans