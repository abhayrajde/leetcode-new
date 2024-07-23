class Solution(object):
    def frequencySort(self, nums):
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        temp = sorted(hm.items(), key = lambda x: x[0], reverse = True)
        temp = sorted(temp, key = lambda x: x[1])
        res = []
        for i in temp:
            res += [i[0]]*i[1]
        return res

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
