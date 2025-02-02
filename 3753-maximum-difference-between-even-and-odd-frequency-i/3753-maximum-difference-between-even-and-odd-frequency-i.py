class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_frequencies = []
        even_frequencies = []
        for count in freq.values():
            if count % 2 == 1:
                odd_frequencies.append(count)
            else:
                even_frequencies.append(count)
        
        if not odd_frequencies or not even_frequencies:
            return -1
        
        return max(odd_frequencies) - min(even_frequencies)