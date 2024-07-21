class Solution:
    def minimumLength(self, s: str) -> int:
        hashmap = collections.defaultdict(int)
        for ch in s:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
        for key, val in hashmap.items():
            val = val % 2
            hashmap[key] = val
            if hashmap[key] == 0:
                hashmap[key] = 2
        return sum(hashmap.values())