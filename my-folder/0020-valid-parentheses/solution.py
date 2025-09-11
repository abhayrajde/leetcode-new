class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] not in hm:
                stack.append(s[i])
            else:
                if stack and stack[-1] == hm[s[i]]:
                    stack.pop()
                else:
                    return False
        return stack == []
