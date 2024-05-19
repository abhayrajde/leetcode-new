class Solution(object):
    def canPartition(self, nums):
        def dptab():

            for i in range(len(nums)):
                dp[i][0] = True
            
            if nums[0]<=target:
                dp[0][nums[0]] = True 

            for i in range(1,len(nums)):
                for j in range(1,target + 1):
                    notPick = dp[i-1][j]
            
                    pick = False
                    if(j >= nums[i]):
                        pick = dp[i-1][j - nums[i]]
                    dp[i][j] = pick or notPick
                
            # print(dp)
            return dp[len(nums)-1][target]

        def dpmem(ind,target):
            # Step 1: Base Cases
            if(target == 0):
                return True
            if(ind == 0):
                return(target == nums[ind])
            if(dp[ind][target] != -1):
                return dp[ind][target]

            #Step 2: Explore possibilities
            notPick = dpmem(ind-1, target)
            pick = 0
            if(nums[ind] <= target):
                pick = dpmem(ind-1, target - nums[ind])
            
            #Step 3: Return Result
            dp[ind][target] = pick or notPick
            return(dp[ind][target])


        def recursion(ind, target):
            # Step 1: Base Cases
            if(target == 0):
                return True
            if(ind == 0):
                return(target == nums[ind])
            
            #Step 2: Explore possibilities
            notPick = recursion(ind-1, target)
            pick = False
            if(nums[ind] <= target):
                pick = recursion(ind-1, target - nums[ind])
            
            #Step 3: Return Result
            return(pick or notPick)

        # Driver Code
        totSum = sum(nums)
        if(totSum%2 != 0):
            return False

        target = totSum/2
        dp = [[False for i in range(target+1)] for i in range(len(nums))]
        # return dpmem(len(nums)-1,totSum/2)
        return dptab()

        #Neetcode Solution
        # dp = set()
        # dp.add(0)
        # for i in range(len(nums)-1, -1, -1):
        #     nextDP = set()
        #     for t in dp:
        #         nextDP.add(t + nums[i])
        #         nextDP.add(t)
        #     dp = nextDP
        # return True if target in dp else False
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
