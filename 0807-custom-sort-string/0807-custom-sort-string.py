class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = collections.defaultdict(bool)
        res = ""
        for ele in s:
            hashmap[ele] = False
        for i in range(len(order)):
            if order[i] in s and not hashmap[order[i]]:
                val = s.count(order[i])
                res += (order[i] * val)
                hashmap[order[i]] = True
        for j in range(len(s)):
            if s[j] not in order:
                res += s[j]
        return res