class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        mx = 1000000002
        n = len(nums)
        dp = [nums[i] - i for i in range(n)]
        
        dict = {}
        
        curr = 1
        
        dp.sort()
        
        for x in dp:
            dict[x+mx] = curr  # we are going to make this a positive value
            curr+=1
        
        curr+=2
        
        st = [0 for i in range(curr*4)]
        
        pos, val = 0, 0
        
        def update(p, l, r):
            if l>pos or r<pos: return
            if l== r:
                st[p] = max(st[p], val)
                return
            mid, n1, n2 = (l+r)//2, (p+p), p+p+1
            update(n1, l, mid)
            update(n2, mid+1, r)
            st[p] = max(st[n1], st[n2])
        
        def search(p, l, r):
            if l>pos: return 0
            if r<=pos: return st[p]
            
            mid, n1, n2 = (l+r)//2, (p+p), p+p+1
            
            return max(search(n1, l, mid), search(n2, mid+1 ,r))
            
        
        
        ans = -436985634766756
        for i in range(n):
            keep = nums[i] - i + mx
            keep = dict[keep]
            
            pos = keep
            f = search(1, 1, curr)
            f+=nums[i]
            ans = max(ans, f)
            
            val = f
            update(1, 1, curr)
        return ans  
        


