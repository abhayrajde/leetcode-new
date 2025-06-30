class Solution(object):
    def groupAnagrams(self, strs):
        hm = defaultdict(list)

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            hm[temp].append(strs[i])
        return (hm.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
