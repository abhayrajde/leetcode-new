class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        list1 = []
        k = 0
        for i in range(len(s)):
            if s[i] == "(":
                list1.append(s[i])
                stack.append((s[i], k))
                k += 1

            elif s[i] == ")":
                if(stack):
                    stack.pop()
                    list1.append(s[i])
                    k += 1
            
            else:
                list1.append(s[i])
                k += 1
        
        for i in range(len(stack)):
            temp = stack.pop()
            list1.pop(temp[1])

        res = "".join(list1)
        return res

        """
        :type s: str
        :rtype: str
        """
        
