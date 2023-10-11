class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if not digits:
            return 

        def backtrack(i, cur):
            if len(cur) == len(digits):
                result.append(cur)
                return

            for letter in lookup[digits[i]]:
                cur += letter
                backtrack(i + 1, cur)
                cur = cur[:-1]


        result = []
        backtrack(0, "")
        return result
        