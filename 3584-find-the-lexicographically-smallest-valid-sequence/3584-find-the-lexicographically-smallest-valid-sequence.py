class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word2)
        last = [-1] * (n + 1)
        last[n] = len(word1)
        j = n - 1

        # Build the 'last' array from the end of word1 and word2
        for i in range(len(word1) - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = []
        j = 0  # Pointer for word2
        mistake_used = False

        # Iterate over word1 to build the answer
        for i, ch in enumerate(word1):
            if j < n:
                can_use_mistake = not mistake_used and (j == n - 1 or i + 1 <= last[j + 1])
                if ch == word2[j] or can_use_mistake:
                    if ch != word2[j]:
                        mistake_used = True
                    ans.append(i)
                    j += 1

        return ans if j == n else []