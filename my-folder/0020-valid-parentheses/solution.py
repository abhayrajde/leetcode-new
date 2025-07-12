class Solution(object):
    def isValid(self, s):
        hm = { '}': '{', ')': '(', ']': '['}
        # open_brackets = set('{', '[', '(')
        stack = []

        for i in range(len(s)):
            if s[i] in hm:
                if not stack or stack[-1] != hm[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        return True if not stack else False
        """
        :type s: str
        :rtype: bool
        """
        
