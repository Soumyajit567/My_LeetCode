class Solution:
    def minLength(self, s: str) -> int:
        sub = s[:]
        while "AB" in sub or "CD" in sub:  
            for i in range(len(sub) - 1):
                for j in range(i + 1, len(sub) + 1):
                    if sub[i:j] == "AB" or sub[i:j] == "CD":
                        sub = sub[:i] + sub[j:]  
                        break  
                else:
                    continue  
                break  
        return len(sub)