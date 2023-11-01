class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = min(nums1)
        min2 = min(nums2)
        min_num1 = float("inf")
        min_num2 = float("inf")
        if min2 >= min1:
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                        min_num1 = min(min_num1, nums1[i])
                    else:
                        val1 = str(nums1[i])
                        val2 = str(nums2[j])
                        num_str = val1 + val2
                        min_num1 = min(min_num1, int(num_str))
        elif min1 > min2:
            for i in range(len(nums2)):
                for j in range(len(nums1)):
                    if nums2[i] == nums1[j]:
                        min_num2 = min(min_num2, nums2[i])
                    else:
                        val1 = str(nums2[i])
                        val2 = str(nums1[j])
                        num_str = val1 + val2
                        min_num2 = min(min_num2, int(num_str))
        return min(min_num1, min_num2)