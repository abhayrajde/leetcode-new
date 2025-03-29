class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        if len(s) > 12:
            return res

        def backtrack(i, dots, curr):
            if dots == 4 and i == len(s):
                res.append(curr[:-1])
                return
            if dots > 4:
                return 
            
            for j in range(i, min(i+3,len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j+1, dots + 1, curr+s[i:j+1]+".")
        backtrack(0,0,'')
        return res
        
        """
        :type s: str
        :rtype: List[str]
        """
        
