class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        n = len(spaces)

        for i, char in enumerate(s):
            if space_index < n and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(char)
        
        return ''.join(result)