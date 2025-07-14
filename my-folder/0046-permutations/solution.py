class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        isTaken = [False] * len(nums)

        def dfs(curr, isTaken):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not isTaken[i]:
                    isTaken[i] = True
                    curr.append(nums[i])
                    dfs(curr, isTaken)
                    curr.pop()
                    isTaken[i] = False
            
        dfs([],isTaken)
        return res
