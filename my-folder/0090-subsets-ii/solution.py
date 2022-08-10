class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        
        nums.sort()
        subset = []
        def backtrack(curr, subset):
            if(curr>=len(nums)):
                res.append(subset[:])
                return
            
            backtrack(curr + 1, subset + [nums[curr]])
            while curr < len(nums) - 1 and nums[curr] == nums[curr + 1]:
                curr += 1
            backtrack(curr + 1, subset)
        
        backtrack(0, [])
        return res
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
