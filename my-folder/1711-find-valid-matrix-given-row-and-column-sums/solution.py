class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= matrix[r][c]
                colSum[c] -= matrix[r][c]
        return matrix



        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        
