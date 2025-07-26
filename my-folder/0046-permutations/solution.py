class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        isTaken = [False] * len(nums)
        def recursion(currPath, isTaken):
            if len(currPath) == len(nums):
                res.append(currPath[:])
            
            for i in range(len(nums)):
                if not isTaken[i]:
                    isTaken[i] = True
                    currPath.append(nums[i])

                    recursion(currPath, isTaken)
                    #backtrack
                    isTaken[i] = False
                    currPath.pop()
        recursion([], isTaken)
        return res


                
