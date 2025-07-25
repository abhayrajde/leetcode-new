class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # OPTION 1
        # TC: O(N * WLOG(W)) - W is len of word
        # groups = defaultdict(list)

        # for s in strs:
        #     temp = ''.join(sorted(s))
        #     groups[temp].append(s)
        # return list(groups.values())

        # OPTION 2
        # TC: O(N*W) - n = total words, w = avg len of the word
        groups = defaultdict(list)

        for s in strs:

            count = [0] * 26    # as we know there will be only 26 characters lowercase(a-z)
            for c in s:
                count[ord(c) - ord('a')] += 1 #geting ascii value of the character
            groups[tuple(count)].append(s)
        return list(groups.values())
