class Solution(object):
    def twoSum(self, nums, target):
        
        hm = {}
        
        for i in range(len(nums)):
            if((target-nums[i]) in hm):
                return(i,hm[target-nums[i]])
            else:
                hm[nums[i]] = i
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
