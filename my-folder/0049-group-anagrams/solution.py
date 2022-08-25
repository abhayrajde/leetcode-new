class Solution(object):
    def groupAnagrams(self, strs):
        hm = {}
        for i in range(len(strs)):
            word = str(sorted(strs[i]))
            if(word not in hm):
                hm[word] = []
            hm[word].append(strs[i])
            
        res = []
        for lists in hm.values():
            res.append(lists)
        return res
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
