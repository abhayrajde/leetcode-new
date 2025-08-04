class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, (i - stack[-1]))
        return res
        
        # WRONG SOLUTION -
        # stack = []
        # maxCounter = 0
        # counter = 0

        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append((i, s[i]))
        #     elif stack and s[i] == ')':
        #         previ, prevEl = stack.pop()
        #         maxCounter = max(maxCounter, (i - previ + 1))
        # return maxCounter
