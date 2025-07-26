class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # OPTION 1 - SLIDING WINDOW
        l, r = 0,0
        zeroCount = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res


        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        
        return r - l + 1
