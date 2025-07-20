class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = defaultdict(int)
        for i, c in enumerate(s):
            hm[c] = i
        
        res = []
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(end, hm[s[i]])
            
            if i == end:
                res.append(size)
                size = 0
        return res
        

