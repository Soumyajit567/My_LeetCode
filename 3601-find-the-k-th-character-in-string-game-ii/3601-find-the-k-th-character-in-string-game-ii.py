class Solution:
    def kthCharacter(self, k: int, op: List[int]) -> str:
        l = 1
        for n in op:
            l *= 2
        c = 0  
        for n in reversed(op):
            l //= 2  
            if k > l:
                k -= l
                if n == 1:
                    c = (c + 1) % 26  

        res = (ord('a') - ord('a') + c) % 26 + ord('a')
        return chr(res)