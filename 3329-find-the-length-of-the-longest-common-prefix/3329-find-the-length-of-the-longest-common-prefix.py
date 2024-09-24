class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashmap = {}
        for n in arr1:
            str1 = str(n)
            prefix = ""
            for ch in str1:
                prefix += ch
                hashmap[prefix] = hashmap.get(prefix, 0) + 1
        max_len = 0
        for n in arr2:
            str2 = str(n)
            prefix = ""
            for ch in str2:
                prefix += ch
                if prefix in hashmap:
                    max_len = max(max_len, len(prefix))
        return max_len