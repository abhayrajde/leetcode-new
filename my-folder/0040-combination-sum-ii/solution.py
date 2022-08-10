class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        
        subset = []
        candidates.sort()
        
        def backtrack(curr, subset, total):
            # subset.append(nums[curr])
            if(total == target):
                res.append(subset)
                return
            
            if(curr==len(candidates) or total > target):
                return
            
            backtrack(curr+1,subset+[candidates[curr]], total+candidates[curr])
            
            while(curr+1<len(candidates) and candidates[curr] == candidates[curr+1]):
                curr+=1
            backtrack(curr+1, subset, total)
        backtrack(0,subset,0)
        return(res)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
