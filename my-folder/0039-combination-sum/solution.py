class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSum, subset):
            if currSum == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or currSum > target:
                return
            

            pick = dfs(i, currSum + candidates[i], subset + [candidates[i]])
            notPick = dfs(i+1, currSum, subset)
        dfs(0,0,[])
        return res

