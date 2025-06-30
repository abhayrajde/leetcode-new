class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
