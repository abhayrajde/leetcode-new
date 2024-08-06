class Solution(object):
    def kthDistinct(self, arr, k):
        hm = defaultdict(int)
        for i in arr:
            hm[i] += 1
        distinctSet = set()
        for i in hm.items():
            if i[1] == 1:
                distinctSet.add(i[0])
        count = 0
        for i in arr:
            if(i in distinctSet):
                count += 1
            if(count == k):
                return i
        return ""
        
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
