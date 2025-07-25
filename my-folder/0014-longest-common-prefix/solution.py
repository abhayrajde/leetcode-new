class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # OPTION 1
        if not strs:
            return ""

        i = 0
        while True:
            for s in strs:
                if i >= len(s): return s[:i]
                if strs[0][i] != s[i]:
                    return s[:i]
            i += 1
        
        # OPTION 2
        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
