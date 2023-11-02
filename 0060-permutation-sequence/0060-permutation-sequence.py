class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Calculate factorials for numbers 1 through n
        factorials = [1]
        for i in range(1, n+1):
            factorials.append(factorials[-1] * i)
        print(factorials)
            
        # Available numbers to pick from
        numbers = list(range(1, n+1))
        k -= 1  
        ans = []
        print(numbers)
        for i in range(n, 0, -1):
            index = k // factorials[i-1]
            ans.append(numbers.pop(index))
            print(" ")
            print(ans)
            k %= factorials[i-1]
        
        return ''.join(map(str, ans))









"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = "".join([str(i) for i in range(1, n + 1)])
        res = []
        def backtrack(num):
            nonlocal res
            if len(num) == n: 
                if len(set(num)) == n:
                    res.append(int(num))
                return
            else:
                for i in range(1, n + 1):
                    if str(i) not in num:
                        backtrack(num + str(i))
 
        for i in range(1, n + 1):
            backtrack(str(i))
        res.sort()
        return str(res[k - 1])
"""