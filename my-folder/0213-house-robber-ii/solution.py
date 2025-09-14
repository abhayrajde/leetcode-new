class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: Tabulation - Space Optimized
        def dptab(nums):
            prev2, prev = 0, nums[0]
            for i in range(1, len(nums)):
                pick = nums[i] + prev2
                notPick = prev

                curr = max(pick, notPick)

                prev2, prev = prev, curr
            return prev
        
        #Driver Code
        if len(nums) < 2:
            return nums[0]
            
        # Exclude first element
        nums1 = nums[1:]
        
        # Exclude last element
        nums2 = nums[:len(nums)-1]
        return max(dptab(nums1), dptab(nums2))
        
        #--------------------------------------

        # DP: Memoization
        def dpmem(ind, numList):
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            pick = numList[ind] + dpmem(ind - 2, numList)
            notPick = dpmem(ind - 1, numList)

            dp[ind] = max(pick, notPick)
            return dp[ind]

        #Driver Code
        ind = len(nums) - 2
        if ind < 0:
            return nums[0]

        dp = [-1] * (len(nums) - 1)
        nums1 = nums[:len(nums) - 1]
        excludeLast = dpmem(ind, nums1)

        dp = [-1] * (len(nums) - 1)
        nums2 = nums[1:]
        excludeFirst = dpmem(ind, nums2)
        return max(excludeLast, excludeFirst)

