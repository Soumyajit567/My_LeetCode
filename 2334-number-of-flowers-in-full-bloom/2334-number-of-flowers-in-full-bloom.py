class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        def binary_search(arr, target):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low  

        # Prepare starts and ends lists as before
        starts, ends = [], []
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)  # '+1' to handle the inclusive end time
        starts.sort()
        ends.sort()

        # Initialize the answer list
        ans = []

        # Process each person's arrival
        for person in people:
            start_count = binary_search(starts, person)
            end_count = binary_search(ends, person)
            # The number of flowers in bloom is the difference between those two counts
            ans.append(start_count - end_count)

        return ans

"""
starts = [1, 3, 4, 9]  # sorted start times
ends = [7, 8, 13, 14]  # sorted end times (original end times + 1)
people = [2, 3, 7, 11]


For each person's arrival time in people, we perform a binary search on starts and ends. Let's break down the binary search iterations for each case:

Person arriving at time 2:

binary_search(starts, 2):

Initial low = 0, high = 3 (indices of the starts array).
First iteration: mid = 1, value at starts[1] is 3 which is greater than 2, so high becomes 0.
Second iteration: low is now greater than high, so the loop ends, and it returns low which is 1.
This means one flower (at index 0) has started blooming by time 2.

binary_search(ends, 2):

Initial low = 0, high = 3 (indices of the ends array).
First iteration: mid = 1, value at ends[1] is 8 which is greater than 2, so high becomes 0.
Second iteration: low is now greater than high, so the loop ends, and it returns low which is 0.
This means no flowers have stopped blooming by time 2.

start_count = binary_search(starts, 2)  # returns 1, because there's 1 start time (1) less than or equal to 2
end_count = binary_search(ends, 2)  # returns 0, because there are 0 end times less than or equal to 2
ans.append(1 - 0)  # ans = [1]



Person arriving at time 3:

binary_search(starts, 3):

Initial low = 0, high = 3.
First iteration: mid = 1, value at starts[1] is 3, equal to 3, so low becomes 2.
Second iteration: low is now greater than high, so the loop ends, and it returns low which is 2.
This indicates that two flowers (at indices 0 and 1) have started blooming by time 3.

binary_search(ends, 3):

Initial low = 0, high = 3.
First iteration: mid = 1, value at ends[1] is 8, greater than 3, so high becomes 0.
Second iteration: low is now greater than high, so the loop ends, and it returns low which is 0.
This means no flowers have stopped blooming by time 3.

start_count = binary_search(starts, 3)  # returns 2, because there are 2 start times (1, 3) less than or equal to 3
end_count = binary_search(ends, 3)  # returns 0, because there are 0 end times less than or equal to 3
ans.append(2 - 0)  # ans = [1, 2]


Person arriving at time 7:

binary_search(starts, 7):

Initial low = 0, high = 3.
First iteration: mid = 1, value at starts[1] is 3, which is less than 7, so low becomes 2.
Second iteration: mid = 2, value at starts[2] is 4, which is less than 7, so low becomes 3.
Third iteration: low is now greater than high, so the loop ends, and it returns low which is 3.
This indicates that three flowers (at indices 0, 1, and 2) have started blooming by time 7.

binary_search(ends, 7):

Initial low = 0, high = 3.
First iteration: mid = 1, value at ends[1] is 8, greater than 7, so high becomes 0.
Second iteration: low is now greater than high, so the loop ends, and it returns low which is 1.
This means one flower (at index 0) has stopped blooming by time 7.

start_count = binary_search(starts, 7)  # returns 3, because there are 3 start times (1, 3, 4) less than or equal to 7
end_count = binary_search(ends, 7)  # returns 1, because there's 1 end time (7) less than or equal to 7
ans.append(3 - 1)  # ans = [1, 2, 2]


Person arriving at time 11:

binary_search(starts, 11):

Initial low = 0, high = 3.
First iteration: mid = 1, value at starts[1] is 3, which is less than 11, so low becomes 2.
Second iteration: mid = 2, value at starts[2] is 4, which is less than 11, so low becomes 3.
Third iteration: mid = 3, value at starts[3] is 9, which is less than 11, so low becomes 4.
Fourth iteration: low is now greater than high, so the loop ends, and it returns low which is 4.
This indicates that all four flowers have started blooming by time 11.

binary_search(ends, 11):

Initial low = 0, high = 3.
First iteration: mid = 1, value at ends[1] is 8, which is less than 11, so low becomes 2.
Second iteration: mid = 2, value at ends[2] is 13, which is greater than 11, so high becomes 1.
Third iteration: low is now greater than high, so the loop ends, and it returns low which is 2.
This means two flowers (at indices 0 and 1) have stopped blooming by time 11.

start_count = binary_search(starts, 11)  # returns 4, because there are 4 start times (1, 3, 4, 9) less than or equal to 11
end_count = binary_search(ends, 11)  # returns 2, because there are 2 end times (7, 8) less than or equal to 11
ans.append(4 - 2)  # ans = [1, 2, 2, 2]


Final Output:

By subtracting the number of flowers that have ended blooming from those that have started by each person's arrival time, we get the final list [1, 2, 2, 2], indicating the number of flowers in bloom when each person arrives.



"""