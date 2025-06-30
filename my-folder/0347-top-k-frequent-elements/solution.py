class Solution(object):
    def topKFrequent(self, nums, k):
        hm = defaultdict(int)
        res = []
        for i in range(len(nums)):
            hm[nums[i]] += 1
        temp = sorted(hm.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            res.append(temp[i][0])
        return res

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
