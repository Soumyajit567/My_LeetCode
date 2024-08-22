class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]
        for ch in range(len(binary_num)):
            if binary_num[ch] == "0":
                binary_num = binary_num[:ch] + "1" + binary_num[ch + 1:]
            else:
               binary_num = binary_num[:ch] + "0" + binary_num[ch + 1:]
        return int(binary_num, 2)