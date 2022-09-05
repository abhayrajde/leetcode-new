class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        
        curr = []
        def backtrack(ind):
            if (sum(curr) == target):
                res.append(curr[:])
                return
            
            if(ind>=len(candidates) or sum(curr)>target):
                return
            
            curr.append(candidates[ind])
            
            backtrack(ind+1)
            
            while(ind<len(candidates)-1 and candidates[ind] == candidates[ind+1]):
                ind+=1
            
            curr.pop()
            
            backtrack(ind+1)
        backtrack(0)
        return res
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
