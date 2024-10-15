class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        cache = {}
        maxF = 0
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
            if cache[n] > maxF:
                    maxF = cache[n]
        
        freqs = {}
        for n in cache:
            f = cache[n]
            if f in freqs:
                freqs[f].append(n)
            else:
                freqs[f] = [n]
        
        output = []
        for i in range(maxF, 0, -1):
            if i in freqs:
                output.extend(freqs[i])
            if len(output) == k:
                break
        return output
