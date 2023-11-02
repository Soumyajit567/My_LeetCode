class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
         if len(s)<10:
            return []
         else:
            ans=set()
            dict1={}
            for i in range(len(s)-9):
                temp=s[i:i+10]
                if temp not in dict1:
                    dict1[temp]=1
                else:
                    dict1[temp]+=1
                    ans.add(temp)
            return list(ans)    