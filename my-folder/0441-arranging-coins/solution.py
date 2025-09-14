class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Optimized - Gauss's Algorithm
        # TC - O(logN)
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res

        # Brute Force 
        # TC - O(N)
        remaining = n
        stairs = 0
        currNeeded = 1
        while currNeeded <= remaining:
            remaining -= currNeeded
            stairs += 1
            currNeeded += 1
        return stairs

            


