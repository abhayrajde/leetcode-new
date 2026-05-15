class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(ind, comb, currSum):
            if currSum == target:
                res.append(comb[:])
                return
            if ind == len(candidates) or currSum > target:
                return 

            pick = dfs(ind, comb+[candidates[ind]], currSum + candidates[ind])
            notPick = dfs(ind+1, comb, currSum)
        dfs(0,[],0)
        return res
