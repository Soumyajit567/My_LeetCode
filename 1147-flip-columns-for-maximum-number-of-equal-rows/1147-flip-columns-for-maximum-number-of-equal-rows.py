class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)
        
        for row in matrix:
            base_pattern = tuple(val == row[0] for val in row)
            
            patterns[base_pattern] += 1
        
        return max(patterns.values())