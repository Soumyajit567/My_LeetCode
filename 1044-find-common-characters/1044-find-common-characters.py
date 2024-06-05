class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        count = 0
        prev_map = {}
        word = words[0]
        for ch in range(len(word)):
            if word[ch] not in prev_map:
                prev_map[word[ch]] = 1
            else:
                prev_map[word[ch]] += 1
        for w in range(1, len(words)):
            hashmap = {}
            for ch in range(len(words[w])):
                if words[w][ch] not in hashmap:
                    hashmap[words[w][ch]] = 1
                else:
                    hashmap[words[w][ch]] += 1
            common_elements = {}
            for char in prev_map:
                if char in hashmap:
                    min_val = min(hashmap[char], prev_map[char])
                    common_elements[char] = min_val
            prev_map.clear()
            prev_map.update(common_elements)
        for key, val in common_elements.items():
            for l in range(val):
                res.append(key)
                
        return res