class Solution(object):
    def isAnagram(self, s, t):

        if(len(s) != len(t)):
            return False

        hms = defaultdict(int)
        hmt = defaultdict(int)

        for i in s:
            hms[i] += 1
        
        for i in t:
            hmt[i] += 1

        for i in s:
            if(i not in hmt or hms[i] != hmt[i]):
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
