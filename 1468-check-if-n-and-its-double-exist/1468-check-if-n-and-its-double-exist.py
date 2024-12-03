class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        boolean = False
        if all(x == 0 for x in arr): return True 

        else:
            count_zeros = 0
            for n in arr:
                if n == 0:
                    count_zeros += 1
                    continue
                elif n > 0 or n < 0:
                    double = 2 * n
                    # print(double)
                    if double in arr:
                        return True
            return True if count_zeros > 1 else False