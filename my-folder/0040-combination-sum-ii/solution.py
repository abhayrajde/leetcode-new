class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, currSum, subset):
            # Base Case
            if currSum == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or currSum > target:
                return 

            pick = dfs(i+1, currSum + candidates[i], subset + [candidates[i]])

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            notPick = dfs(i+1, currSum, subset)

        dfs(0,0,[])
        return res



            
