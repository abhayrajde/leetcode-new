class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        count = 0
        for i in range(len(s)):
            if(s[i] == '('):
                stack.append(s[i])
            
            if(s[i] == ')'):
                if(len(stack) > 0):
                    stack.pop()
                else:
                    count += 1
        return (count + len(stack))
        """
        :type s: str
        :rtype: int
        """
        
