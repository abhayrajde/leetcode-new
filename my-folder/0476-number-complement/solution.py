class Solution(object):
    def findComplement(self, num):
        bit = 0
        todo = num
        while todo:
            bit = bit << 1
            bit = bit ^ 1
            todo = todo >> 1
        return bit ^ num
        """
        :type num: int
        :rtype: int
        """
        
