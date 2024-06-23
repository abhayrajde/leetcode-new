class Solution(object):
    def numberOfSubarrays(self, nums, k):
        isOddList = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if(nums[i] % 2 != 0):
                isOddList[i] = 1

        def function(isOddList, goal):
            # Base Case:
            if(k < 0):
                return 0
            
            l = r = sum1 = oddCount = 0 
            while(r < len(isOddList)):
                sum1 += isOddList[r]

                while(sum1 > goal):
                    sum1 -= isOddList[l]
                    l += 1
                oddCount += r-l+1
                r += 1
            return oddCount
        return(function(isOddList,k) - function(isOddList,k-1))



            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
