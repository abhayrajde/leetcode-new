class Solution:
    def processStr(self, s: str) -> str:
        def remove(s):
            if not s:
                return ""
            return s[:len(s)-1]
        
        def duplicate(s):
            return s + s

        res = ''
        for c in s:
            if c == '*':
                res = remove(res)
            elif c == '#':
                res = duplicate(res)
            elif c == '%':
                res = res[::-1]
            else:
                res += c
        return res

