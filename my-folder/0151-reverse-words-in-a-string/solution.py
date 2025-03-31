class Solution(object):
    def reverseWords(self, s):
        res = ""
        words = []
        curr = ""
        for i in range(len(s)):
            if s[i] == " ":
                if len(curr) > 0:
                    words.append(curr)
                curr = ""
            else:
                curr += s[i]
        if len(curr) > 0:
            words.append(curr)

        for i in range(len(words)-1,-1,-1):
            res += words[i]
            if i > 0:
                res += " "
        return res

        """
        :type s: str
        :rtype: str
        """
        
