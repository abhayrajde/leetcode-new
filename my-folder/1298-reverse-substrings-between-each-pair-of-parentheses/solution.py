class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        result = ""
        count = 0
        for i in range(len(s)):
            if(s[i] == "("):
                stack.append(count)
            
            elif(s[i] == ")"):
                start = stack.pop()
                reversedString = result[start:][::-1]
                result = result[:start] + reversedString

            else:
                result += s[i]
                count += 1
        return result

        """
        :type s: str
        :rtype: str
        """
        
