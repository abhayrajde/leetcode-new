class Solution(object):
    def searchMatrix(self, matrix, target):
        row = 0
        for i in range(len(matrix)):
            # Base Case
            if matrix[i][-1] == target:
                return True
            
            if matrix[i][-1] > target:
                row = i
                break
        l = 0
        r = len(matrix[row])-1
        list1 = matrix[row]
        while l <= r:
            mid = (r+l)//2
            # Base Case
            if list1[mid] == target:
                return True
            
            if list1[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
