class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Step 1: Sort words based on their length
        words.sort(key=len)
        
        # Step 2: Initialize DP dictionary
        dp = {}
        longest_chain_length = 1  # A single word is trivially a chain of length 1

        # Step 3: Process each word in the sorted list
        for word in words:
            dp[word] = 1  # Single word: chain length is 1
            for i in range(len(word)):
                # Form a predecessor by removing the character at index i
                predecessor = word[:i] + word[i+1:]
                
                # If the predecessor is in the dp, and the chain at 'predecessor' + 1 is greater
                # than the current chain at 'word', update the chain at 'word'
                if predecessor in dp and dp[predecessor] + 1 > dp[word]:
                    dp[word] = dp[predecessor] + 1
                    longest_chain_length = max(longest_chain_length, dp[word])

        return longest_chain_length