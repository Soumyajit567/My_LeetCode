class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = 0
        res = [''] * len(s)
        for i in range(len(s)-1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            new_char = (ord(s[i]) - ord('a') + total_shift) % 26 + ord('a')
            res[i] = chr(new_char)
        return ''.join(res)