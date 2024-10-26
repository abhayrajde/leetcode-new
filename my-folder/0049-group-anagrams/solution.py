class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            indexes = [0] * 26
            for c in s:
                n = ord(c) - ord('a')
                indexes[n] += 1
            tup = tuple(indexes)
            if tup in group:
                group[tup].append(s)
            else:
                group[tup] = [s]
        return list(group.values())
