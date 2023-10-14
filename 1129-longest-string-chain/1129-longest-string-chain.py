class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # Step 1: Sort the words by their length.
        words.sort(key=len)
        # Step 2: Create a DP dictionary to store the longest chain for each word.
        dp = {word: 1 for word in words}
        longest = 1

        # Step 3: For each word in the sorted list, iterate through its predecessors.
        for word in words:
            for i in range(len(word)):
                # Generate predecessor by removing one character.
                predecessor = word[:i] + word[i+1:]
                # Step 4: If the predecessor is in the DP dictionary, update the DP entry for the current word.
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            # Step 5: Keep track of the maximum chain length.
            longest = max(longest, dp[word])

        return longest

"""
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
"""