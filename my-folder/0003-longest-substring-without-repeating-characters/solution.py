class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hSet:
                hSet.remove(s[l])
                l += 1
            hSet.add(s[r])
            r += 1
            res = max(res, r-l)
        return res
        """
        :type s: str
        :rtype: int
        """
        
