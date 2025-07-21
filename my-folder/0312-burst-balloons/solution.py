class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #DP MEMOIZATION - TOP DOWN APPROACH - 2ND WAY
        # TC - O(N)**3

        nums = [1] + nums + [1]

        dp = {}

        def dpmem(left,right):
            if left > right:
                return 0

            if (left, right) in dp:
                return dp[(left, right)]

            maxCoins = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dpmem(left, i - 1) + dpmem(i + 1, right)
                maxCoins = max(maxCoins, coins)
            
            dp[(left, right)] = maxCoins
            return dp[(left,right)]
        return dpmem(1, len(nums)-2)
                
        # RECURSION BRUTE FORCE - 1WAY
        def recursion(ind, numList):
            # Base case:
            if not numList or ind >= len(numList):
                return 0

            #Explore all options
            newCoins = numList[ind]
            if ind > 0:
                newCoins *= numList[ind - 1]
            if ind < len(numList) - 1:
                newCoins *= numList[ind + 1]

            notBurst = recursion(ind + 1, numList)
            burst = newCoins + recursion(0, numList[:ind] + numList[ind+1:])

            return max(burst, notBurst)
        return recursion(0, nums)



