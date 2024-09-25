class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hashmap = {}
        for w in words:
            pref = ""
            for ch in w:
                pref += ch
                if pref in hashmap:
                    hashmap[pref] += 1
                else:
                    hashmap[pref] = 1
        ans = []
        for w in words:
            count = 0
            pref = ""
            for ch in w:
                pref += ch
                count += hashmap[pref]
            ans.append(count)
        return ans
