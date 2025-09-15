class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        currPerm = []

        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n,0)

        def recursion():
            if len(currPerm) == len(nums):
                res.append(currPerm[:])
            
            for n in counter:
                if counter[n] > 0:
                    currPerm.append(n)
                    counter[n] -= 1
                    
                    recursion()
                    
                    # Backtrack
                    currPerm.pop()
                    counter[n] += 1

        recursion()
        return res
                
