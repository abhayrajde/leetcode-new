class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DP MEMOIZATION - TOP DOWN APPROACH
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1]*COLS for _ in range(ROWS)]

        def dpmem(r,c, prevVal):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prevVal:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            #possible ways
            up = 1 + dpmem(r-1, c, matrix[r][c])
            down = 1 + dpmem(r+1,c, matrix[r][c])
            left = 1 + dpmem(r,c-1, matrix[r][c])
            right = 1 + dpmem(r,c+1, matrix[r][c])

            dp[r][c] = max(up, down, left, right)
            return dp[r][c]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dpmem(r,c, float("-inf")))
        return res

        # BRUTE FORCE APPROACH - TLE
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        
        def recursion(r,c, prevVal):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or matrix[r][c] <= prevVal:
                return 0
            
            visited.add((r,c))

            #possible ways
            up = 1 + recursion(r-1, c, matrix[r][c])
            down = 1 + recursion(r+1,c, matrix[r][c])
            left = 1 + recursion(r,c-1, matrix[r][c])
            right = 1 + recursion(r,c+1, matrix[r][c])

            visited.remove((r,c))

            return max(up, down, left, right)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, recursion(r,c, float("-inf")))
        return res
