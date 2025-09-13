class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        isTaken = [False] * len(nums)
        res = []

        def recursion(currPath, isTaken):
            if len(currPath) == len(nums):
                res.append(currPath[:])
            
            for i in range(len(nums)):
                if not isTaken[i]:
                    isTaken[i] = True

                    recursion(currPath + [nums[i]], isTaken)
                    
                    # backtrack
                    isTaken[i] = False
        recursion([], isTaken)
        return res
