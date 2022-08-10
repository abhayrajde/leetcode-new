class Solution(object):
    def permute(self, nums):
        res = []
        
        def backtrack(dec_space, curr):
            if(len(curr) == len(nums)):
                res.append(curr)
                return
            
            for i in range(len(dec_space)):
                backtrack(dec_space[:i]+dec_space[i+1:], curr+[dec_space[i]])
        backtrack(nums,[])
        return(res)
                
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
