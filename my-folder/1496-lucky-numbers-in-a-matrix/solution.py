class Solution(object):
    def luckyNumbers (self, matrix):
        res = []
        rowMin = set()
        colMax = set()

        for r in range(len(matrix)):
            rowMin.add(min(matrix[r]))

        for c in range(len(matrix[0])):
            temp = []
            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            colMax.add(max(temp))
        
        for i in rowMin:
            if i in colMax:
                res.append(i)
        return res


        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
