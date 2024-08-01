class Solution(object):
    def countSeniors(self, details):
        count = 0
        for i in details:
            count  += 1 if (int(i[11:13]) > 60) else 0
        return count
        """
        :type details: List[str]
        :rtype: int
        """
        
