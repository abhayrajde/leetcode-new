class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            
            for c in s:
                count[ord(c) - ord("a")]+=1
            
            res[tuple(count)].append(s)
            
        return res.values()
        
#         from collections import defaultdict
#         hm = defaultdict(list)
        
#         hm = {}
#         for i in range(len(strs)):
#             word = str(sorted(strs[i]))
#        #     if(word not in hm):
#         #        hm[word] = []
#             hm[word].append(strs[i])
#         # return list(hm.values())    
#         res = []
#         for lists in hm.values():
#             res.append(lists)
#         return res
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
