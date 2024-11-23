class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)
        
        for row in matrix:
            normal_pattern = tuple(row)
            flipped_pattern = tuple(1 - val for val in row)
            
            patterns[normal_pattern] += 1
            patterns[flipped_pattern] += 1
        
        return max(patterns.values())