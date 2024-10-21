class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        i = 0
        while True:
            for s in strs:
                if s == '': return ''
                if i >= len(s): return strs[0][:i]
                if s[i] != strs[0][i]:
                    return strs[0][:i]

            i += 1
