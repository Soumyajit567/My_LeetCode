class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        n1 = abs(ord('a') - ord(coordinate1[0]))
        n2 = abs(ord('a') - ord(coordinate2[0]))
        
        if (n1 % 2 == 0 and int(coordinate1[1]) % 2 == 1) or (n1 % 2 == 1 and int(coordinate1[1]) % 2 == 0):
            colour1 = "white"
        else:
            colour1 = "black"
        
        if (n2 % 2 == 0 and int(coordinate2[1]) % 2 == 1) or (n2 % 2 == 1 and int(coordinate2[1]) % 2 == 0):
            colour2 = "white"
        else:
            colour2 = "black"
        
        return colour1 == colour2