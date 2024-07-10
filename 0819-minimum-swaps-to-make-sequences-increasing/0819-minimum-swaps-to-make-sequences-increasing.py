class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        no_swap = [float('inf')] * n  
        swap = [float('inf')] * n  

        no_swap[0] = 0
        swap[0] = 1

        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                no_swap[i] = no_swap[i-1]
                swap[i] = swap[i-1] + 1
            
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                no_swap[i] = min(no_swap[i], swap[i-1])  
                swap[i] = min(swap[i], no_swap[i-1] + 1)  

        return min(no_swap[-1], swap[-1])