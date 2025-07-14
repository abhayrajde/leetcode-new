class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base condition
        if not nums:
            return []

        res = []
        def dfs(i, subset):
            if  i >= len(nums):
                res.append(subset[:])
                return
            pick = dfs(i+1, subset + [nums[i]])
            notPick = dfs(i+1, subset)
        dfs(0,[])
        return res
