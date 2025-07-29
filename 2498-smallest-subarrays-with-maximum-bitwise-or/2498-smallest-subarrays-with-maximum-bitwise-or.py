class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        digits = defaultdict(lambda: defaultdict(int))

        for num in set(nums):
            if not num: continue
            d = bin(num)[2:]
            for i, x in enumerate(d[::-1]):
                if x == '1':
                    digits[num][i] += 1
        
        n = len(nums)
        r = n - 1
        ans = [0] * n
        tmp = defaultdict(int)
        for l in reversed(range(n)):
            for x in digits[nums[l]]:
                tmp[x] += 1
            
            # to be removed number will not cause current digits to have zero count after removal
            while r > l and all(tmp[x] > 1 for x in digits[nums[r]]):
                for x in digits[nums[r]]:
                    tmp[x] -= 1
                r -= 1

            ans[l] =  r - l + 1
        
        return ans

# """"
# Initialization and Preprocessing
# Before diving into the main logic, the algorithm begins with creating the digits dictionary. This dictionary holds the bit positions that are set to '1' for each unique number in nums. The purpose of this is to provide an efficient lookup for understanding which bit positions a number will affect when it's added to or removed from a current bitwise OR calculation.

# For the example:

# The unique numbers in nums are {1, 0, 2, 3}
# bin(1) = '0b1' => set bit at position 0
# bin(2) = '0b10' => set bit at position 1
# bin(3) = '0b11' => set bits at positions 0 and 1
# digits would look something like this (ignoring the number 0 as it doesn't affect the OR operation):


# {
#     1: {0: 1},
#     2: {1: 1},
#     3: {0: 1, 1: 1}
# }
# Main Logic
# Setup:
# n stores the length of nums, which is 5 in our case.
# r is initialized to 4, representing the right end of the potential subarray.
# ans is our answer list, initialized as [0, 0, 0, 0, 0].
# tmp is a defaultdict that will store the count of bits in the current OR.
# Iteration over l:
# Now, we begin iterating over the nums in reverse using l as our left pointer.

# First Iteration (l = 4):
# The number at index 4 is 3. digits[3] tells us that bits at positions 0 and 1 are set.
# We update our tmp dict: {0: 1, 1: 1}.
# We check if we can move r to the left (while r > l). The condition inside the while loop checks if all bits in digits[nums[r]] are still present more than once in the current subarray (i.e., it's safe to remove the number at r without affecting the overall OR). This condition is false currently, so r doesn't move.
# ans[l] = r - l + 1 => ans[4] = 1.

# Second Iteration (l = 3):
# The number at index 3 is 1. This affects bit position 0.
# tmp is updated: {0: 2, 1: 1}.
# r still can't move to the left. The condition fails as removing nums[3] will drop the count of the bit at position 0 to 1, and it's not safe.
# ans[3] = 1.

# Third Iteration (l = 2):
# The number at index 2 is 2. This affects bit position 1.
# tmp becomes {0: 2, 1: 2}.
# Now, when we check nums[r] (which is 1), we can safely remove it. Removing 1 will only affect the count of the bit at position 0, but we have it twice. So, r moves left.
# ans[2] = 1.

# Fourth Iteration (l = 1):
# The number at index 1 is 0. This doesn't change our tmp as it doesn't have any set bits.
# We still can't move r left.
# ans[1] = 2.

# Fifth Iteration (l = 0):
# The number at index 0 is 1. This affects bit position 0.
# tmp becomes {0: 3, 1: 2}.
# We still can't move r left.
# ans[0] = 3.
# Finally, the answer is [3, 2, 1, 1, 1].

# The idea behind this sliding window approach is to maintain a running OR of numbers in the subarray. The logic to move the right end of the window (r) is essential. We only move r left when it's safe to do so, ensuring the subarray still produces the maximum OR, and we do this to find the shortest subarray that starts at l and has this maximum OR.
# _______________________________________________________________________________________________________________



# Using the example: nums = [1,0,2,1,3].
# Initialize n = 5, r = 4, ans = [0, 0, 0, 0, 0], and tmp as an empty defaultdict.

# Begin iterating l in reverse:

# For l = 4 (nums[l] = 3):
# tmp updates for bits present in 3: {0: 1, 1: 1}.

# Inner loop to adjust r:

# Currently, r = 4. Checking nums[4] = 3, it has bits {0, 1}. Both bits have a count of 1 in tmp, so we don't decrease r.
# Update answer: ans[4] = r - l + 1 = 1.

# For l = 3 (nums[l] = 1):
# tmp updates for bits present in 1: {0: 2, 1: 1}.

# Inner loop to adjust r:

# r = 4. Checking nums[4] = 3, it has bits {0, 1}. The bit at position 0 only has a count of 2 in tmp, so we don't decrease r.
# Update answer: ans[3] = r - l + 1 = 2.

# For l = 2 (nums[l] = 2):
# tmp updates for bits present in 2: {0: 2, 1: 2}.

# Inner loop to adjust r:

# r = 4. Checking nums[4] = 3, it has bits {0, 1}. Both bits are present in tmp with count greater than 1, so we can safely decrease r to 3.
# Now, r = 3. Checking nums[3] = 1, it has bit {0}. The bit at position 0 only has a count of 2 in tmp, so we don't decrease r further.
# Update answer: ans[2] = r - l + 1 = 2.

# For l = 1 (nums[l] = 0):
# nums[l] = 0 doesn't affect the tmp dictionary.

# Inner loop to adjust r:

# r = 3. Checking nums[3] = 1, it has bit {0}. The bit at position 0 only has a count of 2 in tmp, so we don't decrease r.
# Update answer: ans[1] = r - l + 1 = 3.

# For l = 0 (nums[l] = 1):
# tmp updates for bits present in 1: {0: 3, 1: 2}.

# Inner loop to adjust r:

# r = 3. Checking nums[3] = 1, it has bit {0}. The bit at position 0 has a count of 3 in tmp, so we can safely decrease r to 2.
# Now, r = 2. Checking nums[2] = 2, it has bit {1}. The bit at position 1 only has a count of 2 in tmp, so we don't decrease r further.
# Update answer: ans[0] = r - l + 1 = 3.

# The final answer array becomes [3, 3, 2, 2, 1].

# Through the use of this sliding window approach, by manipulating r while iterating backward through l, we're effectively trying to find the smallest subarray starting at l that has the maximum bitwise OR.

# """"
