class Solution:
    def robotWithString(self, s: str) -> str:
        def getMinChar(freq):
            for f in range(len(freq)):
                if freq[f]>0:
                    return f+97
            return -1
        freq=[0]*26
        for c in s:
            freq[ord(c)-97]+=1
        stack=[]
        ans=''
        for c in s:
            stack.append(c)
            freq[ord(c)-97]-=1
            while stack and ord(stack[-1])<=getMinChar(freq):
                ans+=stack.pop()
        while stack:
            ans+=stack.pop()
        return ans