class Solution:
    def reverse(self, x: int) -> int:
        MIN = - 2147483648
        MAX = 2147483648
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            
            if (res > MAX/10 or (res == MAX and MAX % 10 >= digit)):
                return 0
            elif (res < MIN/10 or (res == MIN and MIN % 10 <= digit)):
                return 0
            else:
                res = (res * 10 + digit)
                if res > MAX or res < MIN:
                    return 0
        return res