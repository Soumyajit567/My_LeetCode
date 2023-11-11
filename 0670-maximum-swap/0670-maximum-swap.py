class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        max_idx = {int(x): i for i, x in enumerate(digits)}
        
        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if max_idx.get(d, -1) > i:
                    digits[i], digits[max_idx[d]] = digits[max_idx[d]], digits[i]
                    return int(''.join(digits))
        
        return num