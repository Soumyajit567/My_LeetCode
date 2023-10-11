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
