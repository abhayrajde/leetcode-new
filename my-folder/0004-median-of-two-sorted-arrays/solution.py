class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []

        while len(nums1) != 0 and len(nums2) != 0:

            if nums1[0] < nums2[0]:
                combined.append(nums1[0])
                del nums1[0]
            else:
                combined.append(nums2[0])
                del nums2[0]
        
        if nums1: combined += nums1
        if nums2: combined += nums2

        n = len(combined)
        if n % 2 == 0:
            return (combined[(n // 2) - 1] + combined[n // 2]) /  2
        else:
            return combined[n // 2]

