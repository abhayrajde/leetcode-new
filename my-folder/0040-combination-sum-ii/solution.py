class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def recursion(ind, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if ind >= len(candidates) or total > target:
                return
            
            #Include
            curr.append(candidates[ind])
            recursion(ind+1, curr, total + candidates[ind])

            curr.pop()
            #Not Include
            while(ind + 1 < len(candidates) and candidates[ind] == candidates[ind+1]):
                ind += 1
            recursion(ind+1, curr, total)
        recursion(0,[],0)
        return res
            
            
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
