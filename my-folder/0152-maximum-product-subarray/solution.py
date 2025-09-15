class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Striver Method - more intuitive
        prefix, suffix = 1, 1

        res = max(nums)
        n = len(nums)

        for i in range(len(nums)):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            
            res = max(res, max(prefix, suffix))
        return res




        # Neetcode Method
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
