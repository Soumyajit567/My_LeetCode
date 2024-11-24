class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        n = len(candies)
        for c in range(k - 1, n):
            hashmap[candies[c]] += 1
        
        best = 0
        
        for i in range(k - 1, n):
            hashmap[candies[i]] -= 1
            if hashmap[candies[i]] == 0:
                del hashmap[candies[i]]
            if i - k >= 0:
                hashmap[candies[i - k]] += 1
            best = max(best, len(hashmap))
        
        return best

