class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        word_dict = {word[::-1]: i for i, word in enumerate(words)}
        res = set()

        for i, word in enumerate(words):
            if word and is_palindrome(word) and "" in word_dict and word_dict[""] != i:
                res.add((i, word_dict[""]))
                res.add((word_dict[""], i))

            for j in range(1, len(word) + 1):
                prefix, suffix = word[:j], word[j:]

                if is_palindrome(prefix) and suffix in word_dict and word_dict[suffix] != i:
                    res.add((word_dict[suffix], i))

                if is_palindrome(suffix) and prefix in word_dict and word_dict[prefix] != i:
                    res.add((i, word_dict[prefix]))

        return list(res)



"""
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for w in range(len(words)):
            new_words = words[:w] + words[w + 1:]
            for k in range(len(new_words)):
                idx = words.index(new_words[k])
                new_s = words[w] + new_words[k]
                if new_s == new_s[::-1]:
                        res.append([w, idx])
        return res
"""