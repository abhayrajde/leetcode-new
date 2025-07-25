class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: N - USING BUCKET SORT
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # TC: NLOGM -> M = DICTIONARY LEN
        res = []
        hm = {}

        for i in nums:
            hm[i] = 1 + hm.get(i, 0)
        
        temp = sorted(hm.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            res.append(temp[i][0])
        return res


