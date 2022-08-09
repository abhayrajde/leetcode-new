class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        tot = []
        def backtrack(curr):
            if(sum(tot) == target):
                res.append(tot[:])
                return
            
            if(curr>=len(candidates) or sum(tot)>target):
                return
                
            tot.append(candidates[curr])
            backtrack(curr)
            
            tot.pop()
            backtrack(curr+1)
        backtrack(0)
        return(res)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
