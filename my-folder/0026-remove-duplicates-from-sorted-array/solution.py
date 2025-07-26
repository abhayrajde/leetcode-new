class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # OPTION 2
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

        # OPTION 1
        l, r = 1, 1 
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l

