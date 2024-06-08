class Solution(object):
    def canPartition(self, nums):
        def dpmem(ind, target):
            # Step 1: Base Case
            if(target == 0):
                return True

            if(ind == 0):
                return(target == nums[ind])

            if(dp[ind][target] != -1):
                return dp[ind][target]
            
            #Step 2: Explore possibilities 
            notPick = dpmem(ind-1,target)

            pick = 0
            if(nums[ind] <= target):
                pick = dpmem(ind-1, target - nums[ind])
            
            dp[ind][target] = pick or notPick
            return dp[ind][target]


        # Drivers Code
        totSum = sum(nums)
        if(totSum%2 != 0):
            return False

        target = totSum/2
        dp = [[-1 for i in range(target+1)] for i in range(len(nums))]
        return dpmem(len(nums)-1, totSum/2)

    
        """
        :type nums: List[int]
        :rtype: bool
        """
        
