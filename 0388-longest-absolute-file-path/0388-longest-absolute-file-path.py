class Solution:
    def lengthLongestPath(self, str_input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in str_input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen