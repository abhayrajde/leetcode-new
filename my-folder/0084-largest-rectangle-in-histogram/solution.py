class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack - increasing monotonic
        stack = [] # pair: (index, height)
        maxArea = 0

        # 3 Possiblities:
        # 1 - prev element > curr element
        # 2 - prev element < curr element
        # 3 - prev element = curr element
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # while scenario 1 is True
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


