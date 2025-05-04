class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = [0] * 1000
        pairs = 0

        for a, b in dominoes:
            key = 10 * min(a, b) + max(a, b)
            pairs += freq[key]
            freq[key] += 1

        return pairs