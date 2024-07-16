class Solution(object):
    def groupAnagrams(self, strs):

        hm = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if(temp not in hm):
                hm[temp] = []
            hm[temp].append(strs[i])
        result = hm.values()
        return result
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
