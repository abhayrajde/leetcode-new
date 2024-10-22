class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        temp = []
        i, j = 0, 0
        n, m = len(mat), len(mat[0])
        for d in range(m + n - 1):
            temp.clear()
            if d < m:
                i = 0
                j = d
            else:
                i = d - m + 1
                j = m - 1
            while i < n and j > -1:
                temp.append(mat[i][j])
                i += 1
                j -= 1
            
            if d % 2 == 0:
                output.extend(temp[::-1])
            else:
                output.extend(temp)
        return output
            

        
