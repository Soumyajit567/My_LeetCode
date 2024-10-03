class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)
        res = [''] * n

        for i in range(n):
            shift = shifts[i] % 26
            shift_array[0] += shift
            if i + 1 < n:
                shift_array[i + 1] -= shift

        total_shift = 0
        for i in range(n):
            total_shift = (total_shift + shift_array[i]) % 26
            new_char = (ord(s[i]) - ord('a') + total_shift) % 26 + ord('a')
            res[i] = chr(new_char)

        return ''.join(res)