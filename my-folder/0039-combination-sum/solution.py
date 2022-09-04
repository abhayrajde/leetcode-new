class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        subset = []
        def backtrack(curr):
            if sum(subset) == target:
                res.append(subset[:])
                return
            
            if(curr>=len(candidates) or sum(subset) > target):
                return
            
            subset.append(candidates[curr])
            backtrack(curr)
            
            subset.pop()
            backtrack(curr+1)
        backtrack(0)
        return res
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
