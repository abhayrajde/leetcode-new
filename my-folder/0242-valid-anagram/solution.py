class Solution(object):
    def isAnagram(self, s, t):
        # base case
        if len(s) != len(t):
            return False

        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        
        for i in range(len(s)):
            hm1[s[i]] += 1
            hm2[t[i]] += 1
        
        for i in hm1.keys():
            if hm1[i] != hm2[i]:
                return False
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
