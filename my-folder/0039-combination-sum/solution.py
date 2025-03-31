class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def recursion(ind, currSum, curr):
            if currSum == target:
                res.append(curr[:])
                return

            if ind == len(candidates) or currSum > target:
                return 
            
            pick = recursion(ind, currSum + candidates[ind], curr[:] + [candidates[ind]])
            notPick = recursion(ind+1, currSum, curr[:])

        recursion(0,0,[])
        return res
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
