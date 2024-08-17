class Solution(object):
    def maxPoints(self, points):
        ROWS, COLS = len(points), len(points[0])
        curr_row = points[0]
        for r in range(1,ROWS):
            next_row = points[r]
            left, right = [0] * COLS, [0] * COLS

            left[0] = curr_row[0]
            for c in range(1, COLS):
                left[c] = max(curr_row[c], left[c-1] - 1)

            right[-1] = curr_row[-1]
            for c in range(COLS - 2, -1, -1):
                right[c] = max(curr_row[c], right[c+1] - 1)

            for c in range(COLS):
                next_row[c] += max(left[c], right[c])

            curr_row = next_row
        return max(curr_row)

        """
        :type points: List[List[int]]
        :rtype: int
        """
        
