class Solution:
    def intToRoman(self, num: int) -> str:
       values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
       symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        # Base case
       if num == 0: return ""

        # Find the largest numeral that fits
       for i, value in enumerate(values):
            if num >= value:
                # Append the symbol for the largest fitting numeral, then recursively solve for the remainder
                return symbols[i] + self.intToRoman(num - value)