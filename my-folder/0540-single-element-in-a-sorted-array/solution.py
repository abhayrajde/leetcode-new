class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums)-1
        while l <= r:
            if len(nums) == 1:
                return nums[0]
            mid = l+r // 2
            if (mid - 1 < 0 or nums[mid] != nums[mid - 1]) and (mid + 1 == len(nums) or nums[mid] != nums[mid + 1]):
                return nums[mid]

            if nums[mid] == nums[mid-1]:
                del nums[mid]
                del nums[mid-1]
            else:
                del nums[mid+1]
                del nums[mid]
            l = 0
            r = len(nums)-1
        """
        :type nums: List[int]
        :rtype: int
        """
        
