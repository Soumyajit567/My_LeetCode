class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)

        def get_char(k, idx, shift):
            if idx < 0:
                return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
            half_len = 1 << idx  # Length of the left half at this level
            if k <= half_len:
                # k is in the left half
                return get_char(k, idx - 1, shift)
            else:
                # k is in the right half
                op = operations[idx]
                if op == 0:
                    # Right half is identical to left half
                    return get_char(k - half_len, idx - 1, shift)
                else:
                    # Right half is left half shifted by +1
                    return get_char(k - half_len, idx - 1, (shift + 1) % 26)

        return get_char(k, n - 1, 0)