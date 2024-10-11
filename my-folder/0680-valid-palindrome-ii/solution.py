class Solution(object):
    def validPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Case 1: Skip the left element
                skipl = s[l+1: r+1]
                if skipl == skipl[::-1]:
                    return True
                # Case 2: Skip the right element
                skipr = s[l:r]
                if skipr == skipr[::-1]:
                    return True
                return False
            else:
                l += 1
                r -= 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
