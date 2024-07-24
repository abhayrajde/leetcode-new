class Solution(object):
    def sortJumbled(self, mapping, nums):
        pairs = []
        for ind, num in enumerate(nums):
            num = str(num)
            mapVal = 0
            for i in num:
                mapVal *= 10
                mapVal += mapping[int(i)]
            pairs.append([mapVal, ind])
        pairs.sort()
        return [nums[p[1]] for p in pairs]

            
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
