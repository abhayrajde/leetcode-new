class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def dfs(ind, subset):
            if ind >= len(nums):
                res.append(subset[:])
                return
            
            pick = dfs(ind + 1, subset + [nums[ind]])
            while ind+1 < len(nums) and nums[ind] == nums[ind+1]:
                ind += 1
            notPick = dfs(ind + 1, subset)

        dfs(0,[])
        return res
        
