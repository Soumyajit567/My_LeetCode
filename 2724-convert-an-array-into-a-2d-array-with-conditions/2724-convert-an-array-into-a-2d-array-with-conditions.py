class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        res = []
        for num in nums:
            while len(res) < freq[num]:
                res.append([])
            for row in res:
                if num not in row:
                    row.append(num)
                    freq[num] -= 1
                    break

        return res