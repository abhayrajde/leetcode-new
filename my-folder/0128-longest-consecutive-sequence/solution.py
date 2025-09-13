class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        nums = list(numSet)
        res = 0
        # we need to figure out if the number we are dealing with, is it the starting number of a sequence
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:   # that means the current number, is the starting of sequence
                counter = 0
                currNum = nums[i]
                while currNum in numSet:
                    counter += 1
                    currNum += 1
                res = max(res, counter)
        return res
                


