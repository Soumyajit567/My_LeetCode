class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays or len(arrays) == 1:
            return 0
        else:
            diff1 = 0
            diff2 = 0
            min_val = float("inf")
            max_val = float("-inf")
            min_arr_no = float("inf")
            max_arr_no = float("-inf")
            for i, arr in enumerate(arrays):
                current_min = min(arr)  
                if current_min < min_val:
                    min_val = current_min
                    min_arr_no = i
            # print(min_val,min_arr_no)
            for i, arr in enumerate(arrays):
                if i != min_arr_no:
                    current_max = max(arr)  
                    if current_max > max_val:
                        max_val = current_max
                        max_arr_no = i
            # print(max_val,max_arr_no)
            diff1 = max_val - min_val
            min_val = float("inf")
            max_val = float("-inf")
            min_arr_no = float("inf")
            max_arr_no = float("-inf")
            for i, arr in enumerate(arrays):
                current_max = max(arr)  
                if current_max > max_val:
                    max_val = current_max
                    max_arr_no = i
            # print(max_val,max_arr_no)
            for i, arr in enumerate(arrays):
                if i != max_arr_no:
                    current_min = min(arr)  
                    if current_min < min_val:
                        min_val = current_min
                        min_arr_no = i
            # print(min_val,min_arr_no)
            diff2 = max_val - min_val
            return max(diff1, diff2)
            



