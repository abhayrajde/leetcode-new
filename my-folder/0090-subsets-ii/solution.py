class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        subset = []
        def backtrack(ind):
            if(ind >= len(nums)):
                res.append(subset[:])
                return
            subset.append(nums[ind])
            backtrack(ind+1)
            
            # while(ind != 0 and nums[ind] == nums[ind-1]):
            while(ind < len(nums) - 1 and nums[ind] == nums[ind + 1]):
                ind+=1
            
            subset.pop()
            backtrack(ind+1)
        backtrack(0)
        return res
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
