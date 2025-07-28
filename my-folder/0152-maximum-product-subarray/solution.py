class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            
            temp1 = currMax * n
            temp2 = currMin * n

            currMax = max(n, temp1, temp2)
            currMin = min(n, temp1, temp2)
            res = max(res, currMax)

        return res
