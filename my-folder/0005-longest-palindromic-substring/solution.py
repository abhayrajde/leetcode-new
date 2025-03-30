class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = [0]
        # def updateLongestPalindrome(l,r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen[0]:
        #             res = s[l:r+1]
        #             resLen[0] = len(res)
        #         l -= 1
        #         r += 1
        for i in range(len(s)):
            # updateLongestPalindrome(i,i)
            # updateLongestPalindrome(i,i+1)
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen[0]:
                    res = s[l:r+1]
                    resLen[0] = len(res)
                l -= 1
                r += 1

            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen[0]:
                    res = s[l:r+1]
                    resLen[0] = len(res)
                l -= 1
                r += 1
        return res
            

        """
        :type s: str
        :rtype: str
        """
        
