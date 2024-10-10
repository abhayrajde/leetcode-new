class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remainder = 0
        for c in s:
            if c == '(':
                remainder += 1
                stack.append(c)
            elif c == ')':
                if remainder == 0: continue
                remainder -= 1
                stack.append(c)
            else:
                stack.append(c)

        output = ''
        while stack:
            cur = stack.pop()
            if cur == '(' and remainder > 0:
                remainder -= 1
                continue
            output += cur
        return output[::-1]

