class Solution(object):
    def topKFrequent(self, nums, k):
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] += 1
        resList = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(resList[i][0])
        return res


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
