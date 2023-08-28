class Solution(object):
    def topKFrequent(self, nums, k):
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        hm = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        results = []
        for i in range(k):
            results.append(hm[i][0])
        return results
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
