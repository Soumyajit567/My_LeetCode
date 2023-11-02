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
## Problem Breakdown for n = 4, k = 9

### Initial Setup
- **numbers**: `[1, 2, 3, 4]`
- **ans**: `""`
- Adjust `k` to 0-index: `k = 9 - 1 = 8`
- **factorial_list**: `[1, 1, 2, 6]` (Precomputed factorials for 0 to n-1)

### Iteration 1
- **fact**: `factorial_list[3] = 6`
- **index**: `8 // 6 = 1`
- Number at index 1 of `numbers`: `2`
- Update **ans**: `ans = "2"`
- Update **numbers**: `[1, 3, 4]`
- Update **k**: `k = 8 % 6 = 2`

### Iteration 2
- **fact**: `factorial_list[2] = 2`
- **index**: `2 // 2 = 1`
- Number at index 1 of `numbers`: `3`
- Update **ans**: `ans = "23"`
- Update **numbers**: `[1, 4]`
- Update **k**: `k = 2 % 2 = 0`

### Iteration 3
- **fact**: `factorial_list[1] = 1`
- **index**: `0 // 1 = 0`
- Number at index 0 of `numbers`: `1`
- Update **ans**: `ans = "231"`
- Update **numbers**: `[4]`
- Update **k**: `k remains 0`

### Iteration 4
- Number at index 0 of `numbers`: `4` (Only number left)
- Update **ans**: `ans = "2314"`

### Final Result
**ans** = "2314" (The 9th permutation of [1, 2, 3, 4])


"""








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