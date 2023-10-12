class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        if len(digits) == 1:
            if digits[0] < 9:
                return [1 + digits[0]]
            else:
                return [1, 0]
        
        else:
            q = deque(digits)
            while q:
                val = q.popleft()
                res += str(val)
        num = int(res)
        num += 1
        string = str(num)
        for k in range(len(string)):
            if k < len(digits):
                digits[k] = int(string[k])
            else:
                digits.append(int(string[k]))
        return digits

