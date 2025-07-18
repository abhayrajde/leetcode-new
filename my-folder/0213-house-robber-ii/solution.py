class Solution:
    def rob(self, nums: List[int]) -> int:
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

