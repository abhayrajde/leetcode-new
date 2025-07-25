class Solution:
    def reorganizeString(self, s: str) -> str:
        hm = {}
        for c in s:
            hm[c] = 1 + hm.get(c,0)
        maxHeap = [[-cnt, el] for el, cnt in hm.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ''
        while maxHeap or prev:
            # Base Case
            if prev and not maxHeap: return ""
            cnt, char =heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt < 0:
                prev = [cnt, char]
        return res
