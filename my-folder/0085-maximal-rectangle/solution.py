class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        heights = [0] * len(matrix[0])
        res = 0

        def solver(heights):
            stack = []
            maxArea = 0
            
            for i, h in enumerate(heights):
                start = i

                while stack and stack[-1][1] > h:
                    previ, prevh = stack.pop()
                    maxArea = max(maxArea, prevh * (i - previ))
                    start = previ
                stack.append((start, h))
            
            for i,h in stack:
                maxArea = max(maxArea, (h * (len(heights) - i)))
            return maxArea

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            res = max(res, solver(heights))
        return res


                    


