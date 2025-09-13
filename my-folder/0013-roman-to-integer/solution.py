class Solution:
    def romanToInt(self, s: str) -> int:
        rome_dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        res = 0
        for i in range(len(s) - 1):
            if rome_dict[s[i]] < rome_dict[s[i+1]]:
                res -= rome_dict[s[i]]
            else:
                res += rome_dict[s[i]]
        res += rome_dict[s[-1]]
        return res
