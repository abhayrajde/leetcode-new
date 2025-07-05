class Solution(object):
    def isPalindrome(self, s):
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        l = 0
        r = len(newStr) - 1
        while l <= r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
