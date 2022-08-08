class Solution(object):
    def subsets(self, nums):
        res = []
        
        subset = []
        def backtrack(curr):
            if(curr>=len(nums)):
                res.append(subset[:])
                return
            
            subset.append(nums[curr])
            backtrack(curr + 1)
            
            subset.pop()
            backtrack(curr+1)
        backtrack(0)
        return(res)
            
            
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
